from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = (
        'member',
        'month',
        'total_amount',
        'payment_status',
        'created_at',
    )

    list_filter = (
        'month',
        'payment_status',
    )

    search_fields = (
        'member__full_name',
        'member__seat_number',
    )

    readonly_fields = (
        'seat_rent_amount',
        'meal_bill_amount',
        'electricity_amount',
        'water_amount',
        'utility_amount',
        'total_amount',
        'created_at',
    )

    ordering = ('-month',)

    fieldsets = (
        ("Member Info", {
            'fields': ('member', 'month')
        }),
        ("Bill Breakdown", {
            'fields': (
                'seat_rent_amount',
                'meal_bill_amount',
                'electricity_amount',
                'water_amount',
                'utility_amount',
                'total_amount',
            )
        }),
        ("Payment", {
            'fields': ('payment_status',)
        }),
        ("System Info", {
            'fields': ('created_at',)
        }),
    )



