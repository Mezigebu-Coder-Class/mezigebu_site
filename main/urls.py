from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

    path('python/', views.python_view, name='python'),
    path('php/', views.php_view, name='php'),
    path('cpp/', views.cpp_view, name='cpp'),
    path('C/', views.C_view, name='C'),
    path('ccp/', views.Cp_view, name='ccp'),
    path('HTML/', views.HTML_view, name='HTML'),
    path('SQL/', views.SQL_view, name='SQL'),
    path('mysqll/', views.MYSQL_view, name='mysqll'),
    path('JavaScript/', views.Java_view, name='JavaScript'),
    path('Java/', views.Java_view, name='Java'),
    path('DataStructre/', views.DataStructre_view, name='DataStructre'),
     path('Compiler/', views.Compiler_view, name='Compiler'),
 
]


