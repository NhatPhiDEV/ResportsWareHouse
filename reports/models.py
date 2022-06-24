from django.db import models
from category.models import BaseModel,Reports_Category

class Reports(BaseModel):
    reports_name = models.CharField(max_length=102, null=False, unique=True)
    reports_category = models.ForeignKey(Reports_Category,related_name='reports_category',on_delete=models.CASCADE)
    class Meta:
        db_table = 'table_reports'

    def __str__(self):
        return self.reports_name

class AllCode(BaseModel):
    table_code = models.CharField(max_length=102, null=False)
    table_name = models.CharField(max_length=102,default='', null=False)
    key_code = models.CharField(max_length=102, null=False, unique=True)
    value_code = models.CharField(max_length=102, null=False, unique=True)
    class Meta:
        db_table = 'table_allcode'

    def __str__(self):
        return self.value_code

class Departments(BaseModel):
    departments_name = models.CharField(max_length=102, null=False, unique=True)
    class Meta:
        db_table = 'table_departments'

    def __str__(self):
        return self.departments_name

class Reports_Month(BaseModel):
    month_name = models.CharField(max_length=102, null=False, unique=True)
    quarter = models.CharField(max_length=102, null=False) 

    class Meta:
        db_table = 'table_month'
    def __str__(self):
        return self.month_name

class Reports_Date(BaseModel):
    day = models.CharField(max_length=102, null=False)
    year = models.CharField(max_length=102, null=False)
    month = models.ForeignKey(Reports_Month,on_delete=models.CASCADE,related_name='reports_month')
    class Meta:
        db_table = 'table_date'
    def __str__(self):
        return f'{self.day}-{self.month.month_name}-{self.year}'
class Industry(BaseModel):
    industry_name = models.CharField(max_length=102, null=False, unique=True)
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE,related_name='departments')
    class Meta:
        db_table = 'table_industry'
    def __str__(self):
        return self.industry_name
class Products(BaseModel):
    products_name = models.CharField(max_length=102, null=False, unique=True)
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE,related_name='industry')
    class Meta:
        db_table = 'table_products'
    def __str__(self):
        return self.products_name
class Reports_Revenue(BaseModel):
    total_including_tax = models.CharField(max_length=102, null=False)
    total_excluding_tax = models.CharField(max_length=102, null=False)
    date = models.ForeignKey(Reports_Date,on_delete=models.CASCADE,related_name='revenue_date')
    reports = models.ForeignKey(Reports,on_delete=models.CASCADE,related_name='revenue_reports')
    products = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='revenue_products')
    class Meta:
        db_table = 'table_reports_revenue' 
    def __str__(self):
        return str(self.date)
class Reports_Profit(BaseModel):
    profit = models.CharField(max_length=102, null=False)
    net_profit = models.CharField(max_length=102, null=False)
    gross_profit = models.CharField(max_length=102, null=False)
    date = models.ForeignKey(Reports_Date,on_delete=models.CASCADE,related_name='profit_date')
    products = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='profit_products')
    reports = models.ForeignKey(Reports,on_delete=models.CASCADE,related_name='profit_reports')
    class Meta:
        db_table = 'table_reports_profit'
    def __str__(self):
        return str(self.date)
    