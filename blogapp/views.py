from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.db.models.fields import GenericIPAddressField
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from blogapp.models import Post
from blogapp.forms import SignUpForm
from django.contrib.auth import authenticate, login




def register(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def _login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user')
                messages.info(request, f"You are now logged in as {username}.")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            return HttpResponse("Invalid username or password")
    form = AuthenticationForm()
    return render(request,"login.html",{'form':form})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_at')
    template_name = 'blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'




# Create your views here.
