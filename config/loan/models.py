from django.db import models
from django.contrib.auth.models import User
class LoanApplication(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female')
    ]
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,null=True,blank=True,help_text='Gender')
    MARRIED_CHOICES = [
        ('Yes','Yes'),
        ('No','No')
    ]
    married=models.CharField(max_length=20,choices=MARRIED_CHOICES,null=True,blank=True,help_text='Married Status')
    DEP_CHOICES = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3+", "3+")
    ]
    dependents = models.CharField(max_length=20,choices=DEP_CHOICES,null=True,blank=True,help_text='Dependents')
    EDUCATION_CHOICES=[
        ('Graduate','Graduate'),
        ('Not Graduate','Not Graduate')
    ]
    education=models.CharField(max_length=80,choices=EDUCATION_CHOICES,null=True,blank=True,help_text='Education')
    EMPLOYED_CHOICES=[
        ('Yes','Yes'),
        ('No','No')
    ]
    self_employed=models.CharField(max_length=20,choices=EMPLOYED_CHOICES,null=True,blank=True,help_text='Self Employed')
    applicant_income = models.PositiveIntegerField(default=0)
    coapplicant_income = models.PositiveIntegerField(default=0)
    loan_amount = models.DecimalField(max_digits=10,decimal_places=2)
    loan_amount_term = models.PositiveIntegerField(default=0)
    credit_history = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    AREA_CHOICES = [
        ("Urban", "Urban"),
        ("Rural", "Rural"),
        ("Semiurban", "Semiurban")
    ]
    property_area = models.CharField(max_length=50,choices=AREA_CHOICES,null=True,blank=True,help_text='Area')
    created_at = models.DateTimeField(auto_now_add=True)
    predicted_approved = models.BooleanField(null=True,blank=True)
    predicted_probability = models.FloatField(null=True, blank=True)
    def __str__(self):
            return f"LoanApplication #{self.pk} by {self.user}"