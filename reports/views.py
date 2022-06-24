from rest_framework import viewsets,generics,status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from reports.models import *
from django.db import connection 
from reports.serializer import *
from django.db.models import Q


class ReportsViewSet(viewsets.ViewSet): 
    @swagger_auto_schema(request_body=ParamReportsData)  
    @action(methods=['post'], detail=False, url_path='get-data')
    def get_data(self,request):
        cursor = connection.cursor()
        try:
            if not (params := request.data.get('params')):
                return Response("No data",status=status.HTTP_403_FORBIDDEN)
            cursor.execute('CALL `get_data_fields`(%s)',[params]) 
            columns = cursor.description
            result = [] 
            for value in cursor.fetchall():
                tmp = {columns[index][0]: column for index, column in enumerate(value)}
                result.append(tmp)
            return Response(result,status=status.HTTP_200_OK)
        finally:
            cursor.close()
    @swagger_auto_schema(request_body=PramFilter)
    @action(methods=['post'], detail=False, url_path='filter-data')
    def filter_data(self,request):  # sourcery skip: low-code-quality, remove-redundant-if, remove-unnecessary-else, swap-if-else-branches
        cursor = connection.cursor()
        # Get data in request
        SELECT_PARAM = request.data.get('params')
        # Choose one month or year
        MONTH_PARAM = request.data.get('month')
        YEAR_PARAM = request.data.get('year')
        # Choose two month or two year
        MONTH_PARAM_2 = request.data.get('month2')
        YEAR_PARAM_2 = request.data.get('year2')
        # Departments
        DEPARTMENTS = request.data.get('departments')
        CONDITIONS = ''
        SELECTED = ''
        # logic 
        try:
            # Filter by month (in year)
            if MONTH_PARAM != 'NULL' and YEAR_PARAM != 'NULL' and DEPARTMENTS == MONTH_PARAM_2 == YEAR_PARAM_2 =='NULL':  
                SELECTED = f'{SELECT_PARAM},month_name'
                CONDITIONS = f"year = {YEAR_PARAM} AND month_name = {MONTH_PARAM}"

            elif MONTH_PARAM_2 != 'NULL' and YEAR_PARAM_2 != 'NULL' and DEPARTMENTS == MONTH_PARAM == YEAR_PARAM =='NULL':  
                SELECTED = f'{SELECT_PARAM},month_name'
                CONDITIONS = f"year = {YEAR_PARAM_2} AND month_name = {MONTH_PARAM_2}"

            #  Filter year (display value month in year)
            elif  YEAR_PARAM != 'NULL' and MONTH_PARAM == 'NULL' and DEPARTMENTS == MONTH_PARAM_2 == YEAR_PARAM_2 =='NULL':
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name'
                CONDITIONS = f"year = {YEAR_PARAM} GROUP BY month_name"

            elif  YEAR_PARAM_2 != 'NULL' and MONTH_PARAM == DEPARTMENTS == MONTH_PARAM_2 == YEAR_PARAM =='NULL':
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name'
                CONDITIONS = f"year = {YEAR_PARAM_2} GROUP BY month_name"

            # Filter departments by year
            elif MONTH_PARAM == YEAR_PARAM == MONTH_PARAM_2 == YEAR_PARAM_2 =='NULL' and DEPARTMENTS != 'NULL':
                SELECTED = f'{SELECT_PARAM},year'
                CONDITIONS = f'table_departments.id = {DEPARTMENTS}'

            # Filter by month, year and departments
            elif MONTH_PARAM != 'NULL' and YEAR_PARAM != 'NULL' and DEPARTMENTS != 'NULL' and  MONTH_PARAM_2 == YEAR_PARAM_2 =='NULL':
                SELECTED = f'{SELECT_PARAM},departments_name'
                CONDITIONS = f'year = {YEAR_PARAM} AND month_name={MONTH_PARAM} AND table_departments.id = {DEPARTMENTS}'
 
            elif MONTH_PARAM_2 != 'NULL' and YEAR_PARAM_2 != 'NULL' and DEPARTMENTS != 'NULL' and  MONTH_PARAM == YEAR_PARAM =='NULL':
                SELECTED = f'{SELECT_PARAM},departments_name'
                CONDITIONS = f'year = {YEAR_PARAM_2} AND month_name={MONTH_PARAM_2} AND table_departments.id = {DEPARTMENTS}'

            # Filter by year and departments
            elif MONTH_PARAM == MONTH_PARAM_2 == YEAR_PARAM_2 =='NULL' and YEAR_PARAM != 'NULL' and DEPARTMENTS != "NULL":
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name'
                CONDITIONS = f"year = {YEAR_PARAM} AND table_departments.id = {DEPARTMENTS} GROUP BY month_name"
           
            elif MONTH_PARAM == MONTH_PARAM_2 == YEAR_PARAM =='NULL' and YEAR_PARAM_2 != 'NULL' and DEPARTMENTS != "NULL":
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name'
                CONDITIONS = f"year = {YEAR_PARAM_2} AND table_departments.id = {DEPARTMENTS} GROUP BY month_name"

            elif MONTH_PARAM != 'NULL' and MONTH_PARAM_2 != 'NULL' and YEAR_PARAM != 'NULL' and YEAR_PARAM_2 != 'NULL' and DEPARTMENTS == 'NULL':
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name,year'
                CONDITIONS = f"{YEAR_PARAM} <= year <= {YEAR_PARAM_2} AND {MONTH_PARAM} <= month_name <= {MONTH_PARAM_2}  GROUP BY month_name"
            
            elif MONTH_PARAM != 'NULL' and MONTH_PARAM_2 != 'NULL' and YEAR_PARAM != 'NULL' and YEAR_PARAM_2 != 'NULL' and DEPARTMENTS != 'NULL':
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name,year'
                CONDITIONS = f"{YEAR_PARAM} <= year <= {YEAR_PARAM_2} AND {MONTH_PARAM} <= month_name <= {MONTH_PARAM_2} AND table_departments.id = {DEPARTMENTS}  GROUP BY month_name"
            
            elif MONTH_PARAM == MONTH_PARAM_2 == 'NULL' and YEAR_PARAM != 'NULL' and YEAR_PARAM_2 != 'NULL' and DEPARTMENTS == 'NULL':
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name,year'
                CONDITIONS = f"{YEAR_PARAM} <= year <= {YEAR_PARAM_2}  GROUP BY month_name"
            
            elif MONTH_PARAM == MONTH_PARAM_2 == 'NULL' and YEAR_PARAM != 'NULL' and YEAR_PARAM_2 != 'NULL' and DEPARTMENTS != 'NULL':
                temp = SELECT_PARAM.split(",")
                result_temp = ''.join(f'Sum({value}) AS {value}, ' for value in temp)
                SELECTED = f'{result_temp}month_name,year'
                CONDITIONS = f"{YEAR_PARAM} <= year <= {YEAR_PARAM_2} table_departments.id = {DEPARTMENTS} GROUP BY month_name"
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            # Query sql
            cursor.execute("CALL `filter_data`('"+SELECTED+"', '"+CONDITIONS+"')")
            # Format tuple to json
            columns = cursor.description
            result = []
            for value in cursor.fetchall():
                tmp = {columns[index][0]: column for index, column in enumerate(value)}
                result.append(tmp)
            return Response(result,status=status.HTTP_200_OK)
        finally:
            cursor.close()  

class DepartmentsViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
