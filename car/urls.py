from django.urls import path
from .import views
urlpatterns = [
   path('',views.car_page, name = 'car'),
   path('signup/',views.UserSignupView.as_view(), name = 'signup'),
   path('login/',views.UserLoginView.as_view(), name = 'login'),
   path('logout/',views.UserLogoutView.as_view(), name = 'logout'),
   path('profile/',views.user_profile, name = 'profile'),
   path('update_profile/',views.UpdateUserProfileView.as_view(), name = 'update_profile'),
   path('add-to-profile/<int:car_id>/', views.add_to_profile, name='add_to_profile'),
   path('car/<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),

]
