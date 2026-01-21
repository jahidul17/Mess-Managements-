from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from members.models import MemberProfile


class Meal(models.Model):
    member = models.ForeignKey(
        MemberProfile,
        on_delete=models.CASCADE,
        related_name='meals'
    )
    date = models.DateField()

    breakfast = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )
    lunch = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )
    dinner = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )

    total_meal = models.PositiveSmallIntegerField(default=3)

    class Meta:
        unique_together = ('member', 'date')
        ordering = ['-date']

    def save(self, *args, **kwargs):
        self.total_meal = self.breakfast + self.lunch + self.dinner
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member.full_name} - {self.date} ({self.total_meal})"



# from django.db import models
# from members.models import MemberProfile

# class Meal(models.Model):
#     member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
#     date = models.DateField()

#     meal_count = models.PositiveSmallIntegerField(default=1)  
#     # 0 = off, 1-4 = meal count

#     is_off = models.BooleanField(default=False)

#     class Meta:
#         unique_together = ('member', 'date')

#     def save(self, *args, **kwargs):
#         if self.is_off:
#             self.meal_count = 0
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.member.full_name} - {self.date} ({self.meal_count})"
