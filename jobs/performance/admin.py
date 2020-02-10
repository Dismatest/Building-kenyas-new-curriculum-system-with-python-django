from django.contrib import admin
from .models import Pre_primary_performance, Lower_primary_performance, Upper_primary_performance


class SearchPrePrimary(admin.ModelAdmin):
    search_fields = ['Student_name']

    class Meta:
        model = Pre_primary_performance


class SearchLowerPrimary(admin.ModelAdmin):
    search_fields = ['Student_name']

    class Meta:
        model = Lower_primary_performance


class SearchUpperPrimary(admin.ModelAdmin):
    search_fields = ['Student_name']

    class Meta:
        model = Upper_primary_performance


admin.site.site_header = 'New Curriculum support System Admin Dashboard'
admin.site.register(Pre_primary_performance, SearchPrePrimary)
admin.site.register(Lower_primary_performance, SearchLowerPrimary)
admin.site.register(Upper_primary_performance, SearchUpperPrimary)
