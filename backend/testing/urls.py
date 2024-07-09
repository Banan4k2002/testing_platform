from django.urls import path
from . import views

app_name = 'testing'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('tests/', views.test_list, name='test_list'),
    path('login/', views.login, name='login'),
    path('start_test/', views.start_test, name='start_test'),
    path('question/<int:pk>/', views.question_view, name='question'),
    path('result/<int:pk>/', views.result, name='result'),
    path('exit/', views.exit, name='exit'),
]
