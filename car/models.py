from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"

class CarModel(models.Model):
    img = models.ImageField(upload_to="car/media/uploads/")
    car_name =models.CharField(max_length=50)
    car_price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    brand_name = models.ForeignKey(Brand, on_delete= models.CASCADE)
    

    def __str__(self):
        return f"{self.car_name}"
    

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    cars = models.ManyToManyField(CarModel,blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.car.car_name}"

