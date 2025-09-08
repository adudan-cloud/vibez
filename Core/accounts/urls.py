from django.urls import path
from .import views 

urlpatterns = [
    path('signup/',views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('register/',views.register_view, name='register'),
    path('dashboard/',views.dashboard_view, name='dashboard'),
    path('',views.home_view, name='home'),
    path('about/',views.about_view, name='about'),
    path('feed/',views.feed_view, name='feed'),
    # other paths...
]

