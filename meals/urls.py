from django.urls import path
from .views import MealCreateView, MealListView

urlpatterns = [
    path('create/', MealCreateView.as_view()),
    path('my-meals/', MealListView.as_view()),
]

