from django.shortcuts import render,redirect
from .forms import RegistrationForm,ChangeuserData
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import UpdateView,CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CommentForm
from.models import CarModel,Comment,Profile
# Create your views here.

def car_page(request):
    return render(request,'car.html') 



class UserSignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        messages.success(self.request,'Account created successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,'Information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context




class UserLoginView(LoginView):
    template_name = 'register.html'
    

    def form_valid(self,form):
        messages.success(self.request,'Logged in successful')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.success(self.request,'Login information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy('profile')





class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
    



@login_required
def add_to_profile(request, car_id):
    car = CarModel.objects.get( id=car_id)
    profile = request.user.profile
    if car.quantity > 0:
        profile.cars.add(car)
        car.quantity -= 1
        car.save()
    return redirect('profile')



@login_required
def user_profile(request):
    profile = request.user.profile  
    cars = profile.cars.all() 
    return render(request, 'profile.html', {'cars': cars})



class UpdateUserProfileView(LoginRequiredMixin,UpdateView):
    form_class = ChangeuserData
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Profile updated successfully')
        return response
    







class CarDetailView(DetailView):
    model = CarModel
    pk_url_kwarg = 'car_id'
    template_name = 'car_detail.html'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        car_object = self.get_object()  # Get the CarModel instance
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car_object
            new_comment.save()
            return redirect('car_detail', car_id=self.object.id)
        return self.get(request, *args, **kwargs)  # If the form is invalid, re-render the detail page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(car=self.object)
        context['form'] = CommentForm()
        return context
