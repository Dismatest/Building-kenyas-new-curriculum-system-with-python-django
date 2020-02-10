from django.contrib import admin
from .models import Profile


class SearchProfile(admin.ModelAdmin):
    search_fields = ['user']

    class Meta:
        model = Profile


admin.site.register(Profile, SearchProfile)
