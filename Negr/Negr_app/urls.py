from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutMe', views.about, name='aboutMe'),
    path('page1', views.page1, name='page1'),
    path('page2', views.page2, name='page2'),
    path('page3', views.page3, name='page3'),
    path('filmpage', views.films, name='films'),
   ]
