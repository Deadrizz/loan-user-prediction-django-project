from django.test import TestCase
from django.contrib.auth.models import User
from loan.models import LoanApplication
class LoanModelTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='stas',password='stas2004')
        self.user= user
    def test_str_representation(self):
        application = LoanApplication(user=self.user,gender='Male',married='Yes',dependents='1',education='Graduate',self_employed='Yes',applicant_income=4583,coapplicant_income=1508.0,loan_amount=128.0,loan_amount_term=360.0,property_area='Rural')
        application.save()
        actual = str(application)
        expected = f"LoanApplication #{application.pk} by {self.user}"
        self.assertEqual(actual,expected)