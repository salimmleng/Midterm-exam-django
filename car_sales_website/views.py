from django.shortcuts import render
from car.models import Brand,CarModel

def home(request, brand_slug = None):
    car_data = CarModel.objects.all()
    if brand_slug is not None:
        brand1 = Brand.objects.get(slug = brand_slug)
        car_data = CarModel.objects.filter(brand_name = brand1)
    brands = Brand.objects.all()
    return render(request,'home.html',{'data': car_data,'brand': brands})


