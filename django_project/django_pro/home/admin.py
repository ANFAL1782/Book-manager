from django.contrib import admin
from. models import Teachers,Books,Registor

# Register your models here.
admin.site.register(Teachers)
admin.site.register(Books)
class RegistorAdmin(admin.ModelAdmin):
    list_display = ('id','student_name','student_phone','student_email','Registor_date','Book_name','Registor_on')
admin.site.register(Registor,RegistorAdmin)