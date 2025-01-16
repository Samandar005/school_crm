from django.contrib import admin
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'class_leader')
    search_fields = ('group_name', 'class_leader__first_name', 'class_leader__last_name')
    list_filter = ('class_leader',)


admin.site.register(Group, GroupAdmin)
