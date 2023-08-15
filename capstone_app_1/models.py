from django.db import models

class StudentLoginDetails(models.Model):
        student_id = models.IntegerField('Student ID')
        email = models.EmailField('Email address')
        password = models.CharField(max_length=12, blank=True, null=True)

class Meta:
        db_table="student_Registration_data"                  