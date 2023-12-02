from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, PostModelForm
from .models import PostModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Homepage-i

def home_view(request):
    title = 'Home'
    context = {
        'title':title,
    }
    return render(request, 'blog/home.html', context)


# Qasja e perdoruesve

def login_page(request):
    title = 'Log in'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_view')
        else:
            messages.error(request, f'Username or password incorrect.')

    context = {
        'title':title,
    }
    return render(request, 'blog/accounts/login.html', context)

# Regjistrimi i perdoruesve

def register_page(request):
    title = 'Register'
    form = CreateUserForm()
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if password1 == password2:
            if form.is_valid():
                form.save()
                messages.success(request,f'Yay, Account created successfully.')
                return redirect('login')
        else:
            messages.error(request, f'Passwords do not match.')
    context = {
        'title':title,
        'form': form,
    }
    return render(request, 'blog/accounts/register.html', context)

# Perjashtimi i perdoruesve

def log_out(request):
    logout(request)
    return redirect('login') 



# Shfaqja e postimeve

def post_view(request):
    user = request.user
    title = 'All posts'
    posts = PostModel.objects.all()
    context = {
        'posts':posts,
        'title':title,
    }
    # Nese perdoruesi nuk eshte i authentikuar athere qasja eshte e pamundur 
    if user.is_authenticated:
        return render(request, 'blog/posts/posts.html', context)
    else:
        return redirect('login')

# Shfaqja e nje posti te caktuar

def single_post(request):
    pass

# Shtimi i post-eve

def add_post(request):
    title = 'Add a post'
    form = PostModelForm()
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            instace = form.save(commit=False)
            instace.author = request.user
            instace.save()
            return redirect('posts')
    context = {
        'title':title,
        'form': form,
    }
    return render(request, 'blog/posts/addpost.html', context)

# Editimi i postimeve

def post_edit(request):
    pass

# Fshirja e postimeve

def post_delete(request):
    pass