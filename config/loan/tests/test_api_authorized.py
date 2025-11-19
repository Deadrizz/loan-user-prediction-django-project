from rest_framework.test import APITestCase
from django.urls import reverse
from loan.models import LoanApplication
from django.contrib.auth.models import User


class LoanApplicationAuthorizedTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='stas',password='stas2004')
        self.client.login(username='stas',password='stas2004')
        self.user=user
    def test_unauthorised_user_application(self):
        data = {'gender':'Male','married':'Yes','dependents':'1','education':'Graduate','self_employed':'Yes','applicant_income':4583,'coapplicant_income':1508.0,'loan_amount':128.0,'loan_amount_term':360.0,'property_area':'Rural'}
        request = reverse('loan-list-create')
        response = self.client.post(request,data,format='json')
        expected = response.json()
        self.assertEqual(response.status_code,201)
        assert 'predicted_probability' in expected
        assert 'predicted_approved' in expected
        self.assertEqual(LoanApplication.objects.count(),1)
        self.assertEqual(LoanApplication.objects.first().user,self.user)