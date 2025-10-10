from django.contrib import admin

from loan.models import LoanApplication
@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'user',
            'gender',
            'married',
            'education',
            'applicant_income',
            'loan_amount',
            'created_at'
        ]
    list_filter = ['gender', 'married', 'education', 'self_employed', 'property_area']
    search_fields = ['user__username']