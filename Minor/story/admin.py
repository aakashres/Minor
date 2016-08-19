from django.contrib import admin
from .models import Story, Response, Rating
# Register your models here.

admin.site.register(Story)
admin.site.register(Response)
admin.site.register(Rating)