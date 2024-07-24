from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


def python_view(request):
    return render(request, 'main/python.html')

def php_view(request):
    return render(request, 'main/php.html')

def cpp_view(request):
    return render(request, 'main/cpp.html')
def C_view(request):
    return render(request, 'main/C.html')
def Cp_view(request):
    return render(request, 'main/ccp.html')
def HTML_view(request):
    return render(request, 'main/HTML.html')
def SQL_view(request):
    return render(request, 'main/SQL.html')
def MYSQL_view(request):
    return render(request, 'main/MYSQL.html')
def Java_view(request):
    return render(request, 'main/Java.html')
def JavaScript_view(request):
    return render(request, 'main/JavaScript.html')
def DataStructre_view(request):
    return render(request, 'main/DataStructre.html')
def Compiler_view(request):
    return render(request, 'main/Compiler.html')

# Add similar view functions for other pages

