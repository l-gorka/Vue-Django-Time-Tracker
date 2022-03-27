from django.contrib import admin
from django.urls import path
from tracker import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('wake-up/', views.wake_up, name='wake-up'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('account/', views.user_data, name='login'),
    path('change-password/', views.password_change, name='password-change'),

    path('admin/', admin.site.urls),
    path('project-list/', views.project_list, name='project-list'),
    path('project-list/<str:pk>/update/', views.project_update, name='project-update'),
    path('project-list/<str:pk>/delete/', views.project_delete, name='project-delete'),
    path('project-create/', views.project_create, name='project-create'),

    path('time-entries/', views.time_entry_list, name='time-entries'),
    path('time-entries/<str:pk>/update/', views.TimeEntryUpdate, name='time-entry-update'),
    path('time-entries/<str:pk>/delete/', views.time_entry_delete, name='time-entry-delete'),
    path('time-entry-create/', views.time_entry_create, name='time-entry-create'),

    path('day-entries/', views.day_entries_list, name='day-entries'),
]
