from rest_framework import serializers
from .models import LoanApplication
#создаём сериализаторы для нашего апи в дальнейшем для фронта
class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanApplication
        fields=('id','gender','married','dependents','education','self_employed','applicant_income','coapplicant_income','loan_amount','loan_amount_term','property_area','created_at','predicted_approved','predicted_probability')
        read_only_fields=('created_at', 'predicted_approved', 'predicted_probability')
    def validate_loan_amount(self,value):                       #валідація для суми кредиту
            if value < 0:
                raise serializers.ValidationError('Loan amount  must be at least 0.') # сума кредиту не може бути 0
            return value
    def validate_applicant_income(self,value):                  # валідація для доходу заявника
            if value<0:
                raise serializers.ValidationError('Application income amount  must be at least 0.') # дохід не може бути 0
            return value
    def validate_coapplicant_income(self,value):                # валідація для доходу співзаявника
            if value<0:
                raise serializers.ValidationError('Coapplicant Income income amount  must be at least 0.') # дохід не може бути 0
            return value

    def validate(self, attrs):                                  # валідація для доходу співзаявника та доходу заявника
            ai = attrs.get('applicant_income')
            ci = attrs.get('coapplicant_income')
            married = attrs.get('married')
            if (ai <= 0 or ai is None):
                raise serializers.ValidationError('Need applicant income more than 0')
            if married == 'Yes' and  (ci is None or ci <=0):
                raise serializers.ValidationError('Якщо ви одружені, потрібно вказати дохід співзаявника.') #якщо користувач вказав що він одружений або заміжній то треба вказати дохід співзаявника
            return attrs