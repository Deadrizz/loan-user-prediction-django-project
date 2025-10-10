from django.urls import path
from .views import LoanApplicationListCreateView
urlpatterns = [
    path('', LoanApplicationListCreateView.as_view(), name='loan-list-create'),
]