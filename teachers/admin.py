from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'phone_number', 'email', 'work_experience')


admin.site.register(Teacher, TeacherAdmin)
