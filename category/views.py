from rest_framework.response import Response

from reports.models import AllCode
from .serializers import CategorySerializer
from rest_framework import viewsets,generics,status
from category.models import Reports_Category
from rest_framework.decorators import action
from reports.serializer import ReportsSerializer,AllCodeSerializer
from django.db.models import Q


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Reports_Category.objects.all()
    serializer_class = CategorySerializer
    @action(methods=['get'], detail=True, url_path='reports')
    def get_reports(self, request, pk):
        if (str(pk).isnumeric()):       
            category = Reports_Category.objects.get(pk=pk)
            if (str(category) =='Kinh Doanh'):
                PARAM_REVENUE = 'table_reports_revenue'
                PARAM_PROFIT = 'table_reports_profit'
                allCode = AllCode.objects.filter(Q(table_code=PARAM_REVENUE) | Q(table_code=PARAM_PROFIT))
                return Response(AllCodeSerializer(allCode,many=True).data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)