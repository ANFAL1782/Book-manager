from django.db import models


# Create your models here.
class Teachers(models.Model):
    Teachers_name=models.CharField(max_length=100)
    Teachers_profile=models.TextField()
    Teachers_image=models.ImageField(upload_to='Teachers',default='SOME STRING')
    def __str__(self):
        return self.Teachers_name
class Books(models.Model):
    Books_name=models.CharField(max_length=500)
    Books_class=models.CharField(max_length=300)
    Books_Subject =models.CharField(max_length=300)
    Books_Teachers=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    Books_Discription=models.CharField(max_length=300)
class Registor(models.Model):
    student_name=models.CharField(max_length=500)
    student_phone=models.CharField(max_length=500)
    student_email=models.EmailField()
    Registor_date=models.DateField()
    Book_name=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    Registor_on=models.DateField(auto_now=True)
    def __str__(self):
        return + self.Books_name+  '-Sir'+ self.Books_Teachers
    