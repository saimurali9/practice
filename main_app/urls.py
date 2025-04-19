from django.urls import path
from . import views 


urlpatterns = [
   path('login/',views.login,name='login'),
   path('logout/',views.logout_page,name='logout'),
   path('register/',views.register,name='register'),
   path('',views.home,name='home'),
   path('movies/',views.movies,name='movies'),
   path('tvshow/',views.tvshows,name='tvshows'),
   path('sports/',views.sports,name='sports'),
   path('premium/',views.premium,name='premium'),
]