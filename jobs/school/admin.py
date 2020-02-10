from django.contrib import admin
from .models import Pre_primary, Lower_primary, Upper_primary


class SearchPrePrimary(admin.ModelAdmin):
    search_fields = [" student_name"]

    class Meta:
        model = Pre_primary


class SearchLowerPrimary(admin.ModelAdmin):
    search_fields = [" student_name"]

    class Meta:
        model = Lower_primary


class SearchUpperPrimary(admin.ModelAdmin):
    search_fields = [" student_name"]

    class Meta:
        model = Upper_primary


admin.site.register(Pre_primary, SearchPrePrimary)
admin.site.register(Lower_primary, SearchLowerPrimary)
admin.site.register(Upper_primary, SearchUpperPrimary)
