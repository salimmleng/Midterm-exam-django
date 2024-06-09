from django.urls import path
from .import views
urlpatterns = [
   path('',views.car_page, name = 'car'),
   path('signup/',views.user_signup, name = 'signup'),
   path('login/',views.user_login, name = 'login'),
   path('logout/',views.userlogout, name = 'logout'),
   path('profile/',views.user_profile, name = 'profile'),
   path('add-to-profile/<int:car_id>/', views.add_to_profile, name='add_to_profile'),
   path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]
