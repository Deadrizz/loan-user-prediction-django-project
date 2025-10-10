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
class LoanApplicationListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LoanApplicationSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['created_at']
    ordering_fields = ['applicant_income','created_at']
    search_fields = ['user__username']
    def get_queryset(self):
        return LoanApplication.objects.filter(user=self.request.user).order_by('-created_at')
    def perform_create(self,serializer):
        validated_data = serializer.validated_data
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
            "Credit_History": float(validated_data["credit_history"] or 0.0),
            "Property_Area": validated_data["property_area"]
        }
        df = pd.DataFrame([renamed_data])
        prediction = model.predict(df)
        probability = model.predict_proba(df)[:, 1]
        serializer.save(user=self.request.user,predicted_approved=bool(prediction[0]),predicted_probability=float(probability[0]))
@login_required
def apply_loan_application(request):
    return render(request, 'loan/apply.html')
@login_required
def my_list(request):
    return render(request, 'loan/my_list.html')
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