from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CommentForm,UserUpdateForm,ProfileUpdateForm
from.models import CarModel,Comment,Profile
# Create your views here.

def car_page(request):
    return render(request,'car.html') 


def user_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request,'register.html',{'form': form,'type': 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                messages.success(request,'Logged in successfully')
                login(request,user)
                return redirect('profile')
            
            else:
                messages.warning(request,'Login info is incorrect')
                return redirect('register')
            
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form': form,'type': 'Login'})





def add_to_profile(request, car_id):
    car = CarModel.objects.get( id=car_id)
    profile = request.user.profile
    
    # Decrease quantity by 1
    if car.quantity > 0:
        profile.cars.add(car)
        car.quantity -= 1
        car.save()
    return redirect('profile')





def userlogout(request):
    logout(request)

    return redirect('login')


# class based
class details_view(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'view_details.html'
    context_object_name = 'car'




# modified

def user_profile(request):
    profile = request.user.profile  
    cars = profile.cars.all() 
    return render(request, 'profile.html', {'cars': cars})





def car_detail(request, car_id):
    car = CarModel.objects.get(id=car_id)
    comments = Comment.objects.filter(car=car)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = CommentForm()
    return render(request, 'car_detail.html', {'car': car, 'form': form, 'comments': comments})


