from rest_framework import serializers
from django.utils import timezone
from .models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
        read_only_fields = ('member', 'total_meal')

    def validate(self, attrs):
        request = self.context.get('request')
        today = timezone.localdate()

        meal_date = attrs.get('date')
        if self.instance:
            meal_date = self.instance.date

        if meal_date <= today:
            raise serializers.ValidationError(
                "You can update meals only for future dates."
            )

        return attrs
