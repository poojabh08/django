from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # path('',)
    path('',home_view,name='home'),
    # path('homee/',home_view1),
    path('login/',userlogin),
    # path('contact/',contact),
    path('delete-student/<id>',deletestudent),
    path('edit-student/<id>',editstudent),
    path('create-student/',createstudent),
    #path('',views.home_view),
    path('admin/', admin.site.urls),
]
