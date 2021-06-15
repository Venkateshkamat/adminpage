from student.models import studenttable
from django.contrib import admin

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','age','img')
    list_editable = ('age',)
    list_per_page = 3
    search_fields = ('firstname',)
    list_filter = ('age',)



admin.site.register(studenttable,ImageAdmin)   #to add data in table from admin page



