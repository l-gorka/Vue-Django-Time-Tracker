"""timeTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from tracker import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('account/', views.user_data, name='login'),
    path('change-password/', views.password_change, name='password-change'),

    path('admin/', admin.site.urls),
    path('project-list/', views.project_list, name='project-list'),
    path('project-list/<str:pk>/', views.ProjectView, name='project-view'),
    path('project-list/<str:pk>/update/', views.project_update, name='project-update'),
    path('project-list/<str:pk>/delete/', views.project_delete, name='project-delete'),
    path('project-create/', views.project_create, name='project-create'),

    path('time-entries/', views.time_entry_list, name='time-entries'),
    path('time-entries/<str:pk>/', views.TimeEntryView, name='time-entry'),
    path('time-entries/<str:pk>/update/', views.TimeEntryUpdate, name='time-entry-update'),
    path('time-entries/<str:pk>/delete/', views.time_entry_delete, name='time-entry-delete'),
    path('time-entry-create/', views.time_entry_create, name='time-entry-create'),

    path('day-entries/', views.day_entries_list, name='day-entries'),
    path('filtered-day-entries/', views.filtered_day_entry_list,),
]
