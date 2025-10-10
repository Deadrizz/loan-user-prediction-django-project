from django.urls import path
from .views import apply_loan_application,my_list
urlpatterns = [
    path('apply/', apply_loan_application, name='loan-apply'),
    path("my_list", my_list, name="loan-my")
]