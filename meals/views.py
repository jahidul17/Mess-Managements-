from rest_framework import generics, permissions
from .models import Meal
from .serializers import MealSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Sum

class MealCreateView(generics.CreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(member=self.request.user.memberprofile)
        
        
class MealUpdateView(generics.UpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # member can update ONLY his own meals
        return Meal.objects.filter(member=self.request.user.memberprofile)
    

class MealListView(generics.ListAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Meal.objects.filter(member=self.request.user.memberprofile)

        month = self.request.query_params.get('month')
        if month:
            year, month_num = month.split('-')
            queryset = queryset.filter(
                date__year=year,
                date__month=month_num
            )

        return queryset.order_by('-date')
    

class MonthlyMealCountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        month = request.query_params.get('month')  # "2026-01"

        if not month:
            return Response(
                {"error": "month query param is required (YYYY-MM)"},
                status=400
            )

        try:
            year, month_num = month.split('-')
        except ValueError:
            return Response(
                {"error": "Invalid month format. Use YYYY-MM"},
                status=400
            )

        count = Meal.objects.filter(
            member=request.user.memberprofile,
            date__year=year,
            date__month=month_num
        ).count()

        return Response({
            "month": month,
            "total_meals": count
        })



class KitchenTodayMealView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # or AllowAny if public screen

    def get(self, request):
        today = timezone.localdate()

        data = Meal.objects.filter(date=today).aggregate(
            breakfast=Sum('breakfast'),
            lunch=Sum('lunch'),
            dinner=Sum('dinner'),
        )

        return Response({
            "date": today,
            "breakfast": data['breakfast'] or 0,
            "lunch": data['lunch'] or 0,
            "dinner": data['dinner'] or 0,
            "total_meal": (
                (data['breakfast'] or 0) +
                (data['lunch'] or 0) +
                (data['dinner'] or 0)
            )
        })
