from django.urls import path,include
from . import views

urlpatterns = [

    
    path('auth/login/',views.login_view, name='login'),
    path('auth/logout/',views.logout_view, name='logout'),
    path('auth/signup/',views.signup_view, name='signup'),
    path('editprofile/',views.edit_profile, name='edit_profile'),
    path('userupdate/',views.userupdate, name='userupdate'),
    
    path('follow-user/<slug:account>/',views.follow, name='follow_user'),
    path('unfollow/<slug:slug>/',views.unfollow, name='unfollow_user'),
    path('<slug:slug>/',views.myprofile, name='profile'),
]   