"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from home.views import userlogin,userregister,userlogout
# from home.views import home_view1
#from home import views

urlpatterns = [
    path('home/',include('home.urls')),
    path('login/',userlogin,name='login'),
    path('register/',userregister,name='register'),
    path('logout/',userlogout,name='logout'),
    # path('',home_view1),
    # path('',home_view),
    # path('contact/',contact),
    # path('delete-student/<id>',deletestudent),
    # path('edit-student/<id>',editstudent),
    # path('create-student/',createstudent),
    # #path('',views.home_view),
    # path('admin/', admin.site.urls),
]
