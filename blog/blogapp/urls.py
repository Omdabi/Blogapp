from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name= 'base'),
    path('home/', views.home, name= 'home'),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('addblog/', views.addblog, name = 'addblog'),
    path('showblog/', views.showblog, name = 'showblog'),
    path('delete/<int:did>/',views.delete,name='delete'),
    path('edit/<int:did>/',views.edit,name='edit')
]