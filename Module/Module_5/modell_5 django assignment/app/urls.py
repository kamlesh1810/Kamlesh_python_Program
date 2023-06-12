"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('Admin-password-change/', views.adminPassChange, name='adminPassChange'),
    path('Admin-profile-change/', views.adminProfileChange, name='adminProfileChange'),
    path('Admin-pic-change/', views.adminPicChange, name='adminPicChange'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('all-product/',views.allProduct,name='allProduct'),
    path('search-product/',views.searchProduct,name='searchProduct'),
    path('edit-product/<int:pk>',views.editProduct,name='editProduct'),
    path('update-product/',views.updateProduct,name='updateProduct'),
    path('delete-product/<int:pk>',views.deleteProduct,name='deleteProduct'),
]
