from django.contrib import admin
from .models import SiteEmailLog

# Register your models here.


class SiteEmailLogAdmin(admin.ModelAdmin):
    list_display = ["email", "ip_addr", "created_date"]
    list_filter = ["user_agent", "created_date"]
    readonly_fields = ("created_date", )
    search_fields = ['email', "ip_addr", "user_agent"]
    date_hierarchy = "created_date"
    ordering = ["email", "user_agent", "created_date"]


admin.site.register(SiteEmailLog, SiteEmailLogAdmin)
