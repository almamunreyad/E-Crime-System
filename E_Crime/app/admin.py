from django.contrib import admin
from . models import * 



class FormAdmin(admin.ModelAdmin):
    list_display = ('crim_id', 'name', 'report', 'image')
    
class CriminalAdmin(admin.ModelAdmin):
    list_display = ('criminal_id', 'criminal_name', 'crime_type', 'criminal_image')
    
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

# Register your models here.
admin.site.register(Form, FormAdmin)
admin.site.register(Criminal_List, CriminalAdmin)
admin.site.register(SignUp, SignUpAdmin)
