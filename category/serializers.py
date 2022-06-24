from rest_framework import serializers
from .models import Reports_Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports_Category
        fields = ['id','reports_category_name']