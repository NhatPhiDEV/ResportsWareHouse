from django.db import models

class BaseModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Reports_Category(BaseModel):
    reports_category_name = models.CharField(max_length=102, null=False, unique=True)

    class Meta:
        db_table = 'table_reports_category'

    def __str__(self):
        return self.reports_category_name