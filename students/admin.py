from django.contrib import admin

# Register your models here.
from students.models import Profile, Result

admin.site.register(Profile)
admin.site.register(Result)