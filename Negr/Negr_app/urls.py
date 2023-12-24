from . import views
from django.urls import path
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('test/', views.TestPage.as_view(), name='test'),
    # path('book/', views.Books.as_view(), name='books'),
    # path('register/', views.Registration.as_view(), name='register'),
    # path('user_page/', views.UserView.as_view(), name='user_page'),
    # path('login/', views.Login.as_view(), name='login'),
    # path('logout/', views.Logout.as_view(), name='logout'),
    path('create_project/', views.ProjectCreate.as_view(), name='create_project'),
    path('project/<int:id>/', views.ProjectPage.as_view(), name='project'),
    # path('create_task/', views.CreateProject.as_view(), name='create_task'),
    # path('change_project/<int:id>/', views.change_project, name='project'),
   ]
