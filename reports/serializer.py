from rest_framework import serializers
from reports.models import *

# PARAM
class ParamReportsData(serializers.Serializer):
    params = serializers.CharField( required= False)
class PramFilter(serializers.Serializer):
    params = serializers.CharField( required= False)
    month = serializers.CharField( required= False)
    year = serializers.CharField( required= False)
    departments = serializers.CharField( required= False)

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id','reports_name']
class AllCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCode
        fields = ['table_name','key_code','value_code']
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id','departments_name']