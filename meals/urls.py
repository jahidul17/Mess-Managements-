from django.urls import path
from .views import (
    MealCreateView, 
    MealListView,
    MonthlyMealCountView,
    MealUpdateView,
    KitchenTodayMealView
)

urlpatterns = [
    path('create/', MealCreateView.as_view()),
    path('update/<int:pk>/', MealUpdateView.as_view(), name='meal-update'),
    path('my-meals/', MealListView.as_view()),
    path('count/', MonthlyMealCountView.as_view()),
    path('kitchen/today/', KitchenTodayMealView.as_view(), name='kitchen-today-meal'),

]

