from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    #path('login',views.login_user,name='homelogin'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name="register"),
    path('record/<int:pk>',views.in_record,name="record"),
    path('de_record/<int:pk>',views.de_in_record,name="de_record"),
    path('add_record/',views.add_in_record,name="add_record"),
    path('up_record/<int:pk>',views.up_in_record,name="update_record"),
]
