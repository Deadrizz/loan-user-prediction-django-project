from django.shortcuts import render,redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import LoanApplicationSerializer
from .models import LoanApplication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import LoanApplication
import joblib
import pandas as pd
import os
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
#подключаемся к ML
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(MODEL_PATH)
# @csrf_exempt
# def predict_view(request):
#     if request.method == 'POST':
#         if len(request.body) > 0:
#             data = json.loads(request.body)
#             df = pd.DataFrame([data])
#             prediction = int(model.predict(df)[0])
#             probability = float(model.predict_proba(df)[0,1])
#             return JsonResponse({'prediction': prediction, 'probability': probability})
#         return JsonResponse({'error': 'Request body not found.'})
#     return JsonResponse({'error': 'Method not allowed'})
#класс для нашего сериалайзера
class LoanApplicationListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] #ставимо пермишн клас на авторизований
    serializer_class = LoanApplicationSerializer # підключаемось до нашого сериализатора
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter] # додаємо в апи функції пошуку.фільтраціі та упорядкування
    filterset_fields = ['created_at'] #фільтруємо наші поля по часу створення
    ordering_fields = ['applicant_income','created_at'] #упорядковуємо по доходу та часу створення заявки
    search_fields = ['user__username'] #робимо пошук по імені
    #получаем queryset и фильтруем его по определённому юзеру что бы он видел только свою базу данных
    def get_queryset(self):
        return LoanApplication.objects.filter(user=self.request.user).order_by('-created_at')
    #подключаем модель к нашему джанго проекту
    def perform_create(self,serializer):
        validated_data = serializer.validated_data # валідируємо дані користувачо сгідно нашим валідаторам
        renamed_data = {
            "Gender": validated_data["gender"],
            "Married": validated_data["married"],
            "Dependents": validated_data["dependents"],
            "Education": validated_data["education"],
            "Self_Employed": validated_data["self_employed"],
            "ApplicantIncome": int(validated_data["applicant_income"]),
            "CoapplicantIncome": int(validated_data["coapplicant_income"]),
            "LoanAmount": float(validated_data["loan_amount"]),
            "Loan_Amount_Term": int(validated_data["loan_amount_term"]),
            "Property_Area": validated_data["property_area"]
        } # робимо маппинг щоб мл модель зрозуміла які дані користувача куди підходять
        df = pd.DataFrame([renamed_data]) # створюємо дата фрейм з наших маппенених даних
        prediction = model.predict(df)
        probability = model.predict_proba(df)[:, 1]         # предіктимо стосовно даних користувача
        serializer.save(user=self.request.user,predicted_approved=bool(prediction[0]),predicted_probability=float(probability[0])) #зберігаємо результат
#рендерим нашу страницу предварительно оборачивая её только в залогиненых пользователей
@login_required
def apply_loan_application(request):
    return render(request, 'loan/apply.html')
#рендерим нашу страницу предварительно оборачивая её только в залогиненых пользователей
@login_required
def my_list(request):
    return render(request, 'loan/my_list.html')
#регистрируем нашего пользователя
def register_view(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('loan-apply')
    else:
        form = UserRegisterForm()
    return render(request, 'loan/register.html', {'form': form})