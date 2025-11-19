from rest_framework.test import APITestCase
from django.urls import reverse
from loan.models import LoanApplication


class LoanApplicationUnauthorizedTests(APITestCase):
    def test_unauthorised_user_application(self):
        data = {'gender':'Male','married':'Yes','dependents':'1','education':'Graduate','self_employed':'Yes','applicant_income':4583,'coapplicant_income':1508.0,'loan_amount':128.0,'loan_amount_term':360.0,'property_area':'Rural'}
        request = reverse('loan-list-create')
        response = self.client.post(request,data,format='json')
        self.assertEqual(response.status_code,403)
        self.assertEqual(LoanApplication.objects.count(),0)