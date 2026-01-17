from django.db import models
from members.models import MemberProfile

class Meal(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    date = models.DateField()

    meal_count = models.PositiveSmallIntegerField(default=1)  
    # 0 = off, 1-4 = meal count

    is_off = models.BooleanField(default=False)

    class Meta:
        unique_together = ('member', 'date')

    def save(self, *args, **kwargs):
        if self.is_off:
            self.meal_count = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member.full_name} - {self.date} ({self.meal_count})"
