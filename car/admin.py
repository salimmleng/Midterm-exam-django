from django.contrib import admin
from .models import CarModel,Brand,Profile,Comment
# Register your models here.

admin.site.register(CarModel)
admin.site.register(Brand)
admin.site.register(Profile)
admin.site.register(Comment)



