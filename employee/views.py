
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Employee
from .serializers import EmployeeSerializer,CompanySerializer
from django.db import transaction

class AddDataView(APIView):

    def get(self, request):
        return Response({"message": "GET request successful!"})

    def post(self, request):
        
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"})

        try:
            df = pd.read_excel(file)
            employees = []
            companies = {}
            for _, row in df.iterrows():
                company_name = row['COMPANY_NAME']
                if company_name not in companies:
                    company_serializer = CompanySerializer()
                    company = company_serializer.get_or_create_company(company_name)
                    companies[company_name] = company

                employee_data = {
                    "company": companies[company_name].id,
                    "first_name": row['FIRST_NAME'],
                    "last_name": row['LAST_NAME'],
                    "phone_number": row['PHONE_NUMBER'],
                    "salary": row['SALARY'],
                }
                employees.append(employee_data)

            serializer = EmployeeSerializer(data=employees, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Data uploaded successfully"})
            return Response({"message": "Error while add data"})
        except Exception as e:
            return Response({"error": str(e)})
