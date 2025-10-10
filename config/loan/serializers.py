from rest_framework import serializers
from .models import LoanApplication
class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanApplication
        fields=('id','gender','married','dependents','education','self_employed','applicant_income','coapplicant_income','loan_amount','loan_amount_term','credit_history','property_area','created_at','predicted_approved','predicted_probability')
        read_only_fields=('created_at', 'predicted_approved', 'predicted_probability')
    def validate_loan_amount(self,value):
            if value < 0:
                raise serializers.ValidationError('Loan amount  must be at least 0.')
            return value
    def validate_applicant_income(self,value):
            if value<0:
                raise serializers.ValidationError('Application income amount  must be at least 0.')
            return value
    def validate_coapplicant_income(self,value):
            if value<0:
                raise serializers.ValidationError('Coapplicant Income income amount  must be at least 0.')
            return value

    def validate(self, attrs):
            ai = attrs.get('applicant_income')
            ci = attrs.get('coapplicant_income')
            if (ai <= 0 or ai is None) or (ci is None or ci <=0):
                raise serializers.ValidationError('Need applicant or coapplicant income mor than 0')
            return attrs