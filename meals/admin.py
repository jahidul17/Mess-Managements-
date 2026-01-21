from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('member', 'date', 'breakfast', 'lunch', 'dinner', 'total_meal')
    list_filter = ('date',)
    search_fields = ('member__full_name',)


