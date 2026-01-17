from rest_framework import generics, permissions
from .models import Meal
from .serializers import MealSerializer


class MealCreateView(generics.CreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Logged-in member er jonno auto meal create hobe
        default meal_count = 1
        """
        serializer.save(
            member=self.request.user.memberprofile
        )


class MealListView(generics.ListAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(
            member=self.request.user.memberprofile
        ).order_by('-date')



