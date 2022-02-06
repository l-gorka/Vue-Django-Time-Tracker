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
from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project-list/', views.ProjectList),
    path('project-list/<str:pk>/', views.ProjectView),
    path('project-create/', views.ProjectCreate),
    
    path('time-entries/', views.TimeEntryList),
    path('time-entries/<str:pk>/', views.TimeEntryView),
    path('time-entries/<str:pk>/update/', views.TimeEntryUpdate),
    path('time-entry-create/', views.TimeEntryCreate),

    path('day-entries/', views.DayEntriesList)
]
