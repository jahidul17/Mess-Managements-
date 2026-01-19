from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Bill
from .serializers import BillSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from members.models import MemberProfile as Member
from charges.models import MonthlyCharge
from meals.models import Meal
from .models import Bill
from decimal import Decimal
import datetime

class MemberBillListView(ListAPIView):
    serializer_class=BillSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Bill.objects.filter(member=self.request.user.memberprofile)


class GenerateMonthlyBillView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        month = request.data.get('month')  # "2026-01-01"
        bill_month = datetime.datetime.strptime(month, "%Y-%m-%d").date()

        charges = MonthlyCharge.objects.get(effective_month=bill_month)

        for member in Member.objects.all():
            seat_rent = member.seat_rent
            meal_count = Meal.objects.filter(
                member=member,
                date__year=bill_month.year,
                date__month=bill_month.month
            ).count()

            meal_bill = Decimal(meal_count) * charges.meal_rate

            total = (
                seat_rent +
                meal_bill +
                charges.electricity_bill +
                charges.water_bill +
                charges.utility_charge
            )

            Bill.objects.update_or_create(
                member=member,
                month=bill_month,
                defaults={
                    'seat_rent_amount': seat_rent,
                    'meal_bill_amount': meal_bill,
                    'electricity_amount': charges.electricity_bill,
                    'water_amount': charges.water_bill,
                    'utility_amount': charges.utility_charge,
                    'total_amount': total,
                }
            )

        return Response({"message": "Bills generated successfully"})


