from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from app.forms import UserForm,SignUpForm,PostForm,EventForm
from app.models import PostModel
from django.contrib.auth import authenticate,logout,login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.


def base(request):
    user_all = User.objects.all
    return render(request,'app/base.html',{'user_all':user_all})


def signup(request):
    registered=False
    if request.method=='POST' :
        user_form=UserForm(data=request.POST)
        signup_form=SignUpForm(data=request.POST)
        if user_form.is_valid() and signup_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            if user.last_name == 'AANP' :
                user.is_staff = True
                user.is_superuser = True
            user.save()
            sign_up=signup_form.save(commit=False)
            sign_up.user=user
            sign_up.save()
            registered=True
            return HttpResponseRedirect(reverse('login'))
        else:
            print(user_form.errors,signup_form.errors)
    else:
        user_form=UserForm()
        signup_form=SignUpForm()

    return render(request,'app/SignUp.html',{'user_form':user_form,
                                              'signup_form':signup_form,
                                                'registered':registered,})





# def user_login(request):
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#
#         user = authenticate(username=username,password=password)
#
#         if user:
#
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect('/')
#             else:
#                 return HttpResponse('Your Account is Inactive. Plz create a different account')
#
#         else:
#             return HttpResponse("invalid login details:  username: " + username + " password: " + password)
#
#     else:
#         return render(request, 'registration/login.html', {})



@login_required
def user_logout(request):
     logout(request)
     return HttpResponseRedirect('/accounts/login')


@login_required
def post_form(request,pk):

    user = get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post_filled_form = form.save(commit=False)
            post_filled_form.user = user
            post_filled_form.save()
            return redirect('app:post_detail',pk=user.pk)
    else:
        form = PostForm()

    return render(request, 'app/post_form.html', {'post_filled_form': form})





@login_required
def postdetail(request,pk):
    user = get_object_or_404(User,pk=pk)
    post_model=user.posts.all
    return render(request,'app/post_detail.html',{'post_model':post_model,
                                                  'user':user,})


# class CreatePostView(LoginRequiredMixin,CreateView):
#     login_url = '/login/'
#     redirect_field_name = 'app/post_detail.html'
#     template_name = 'app/post_form.html'
#     form_class = PostForm
#     model = PostModel

# class DetailPostView(DetailView):
#      template_name = 'app/post_detail.html'
#      model = PostModel





# def show_allpost(request):
#     user=User.objects.all
#     return render(request,'app/base.html',{'all_user':user})



@login_required
def event_form(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            eventform=form.save(commit=False)
            eventform.user = user
            eventform.save()
            return redirect('app:event_detail', pk=user.pk)
    else:
        form = EventForm()


    return render(request,'app/user_event_form.html',{'form':form,
                                                'user':user,})

@login_required
def event_detail(request,pk):
    user=get_object_or_404(User,pk=pk)
    event_data=user.events.all()
    return render(request,'app/user_event_detail.html',{'user':user,
                                                  'event_data':event_data,})