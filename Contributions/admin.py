from django.contrib import admin
from .models import Classification_large,Classification_middle,Classification_small

admin.site.register(Classification_large)
admin.site.register(Classification_middle)
admin.site.register(Classification_small)
