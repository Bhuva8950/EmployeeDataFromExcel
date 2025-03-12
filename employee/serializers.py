from rest_framework import serializers
from .models import Company, Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

    def get_or_create_company(self, company_name):
        company_data = {"name": company_name}
        serializer = self.__class__(data=company_data)

        if serializer.is_valid():
            company, created = Company.objects.get_or_create(name=company_name)
            return company
        else:
            raise serializers.ValidationError(serializer.errors)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'company', 'first_name', 'last_name', 'phone_number','salary']
