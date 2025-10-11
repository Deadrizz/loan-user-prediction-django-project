from django.urls import path
from .views import LoanApplicationListCreateView
#урлы для апи
urlpatterns = [
    path('', LoanApplicationListCreateView.as_view(), name='loan-list-create'),
]