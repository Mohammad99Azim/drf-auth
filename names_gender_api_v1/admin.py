from django.contrib import admin

from .models import Names_Gender
# Register your models here.
class Custom_Names_Gender(admin.ModelAdmin):
    list_display = ['the_name','gender','accurate']
    search_fields = ['the_name']
    list_filter = ['gender','accurate']

admin.site.register(Names_Gender,Custom_Names_Gender)
