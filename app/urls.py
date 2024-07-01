from django.urls import path, include
from . import views # Correcto
from rest_framework import permissions
from rest_framework.routers import DefaultRouter  # Correcto
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import TaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
from .views import RegisterUserView


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Task API",
        default_version='v1',
        description="API documentation for the Task management app",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", views.index, name="index"),
    path("task-list/", views.task_list, name="task_list"),
    #path("task-detail/<int:task_id>/", views.task_detail, name="task_detail"),
    path("new-task/", views.new_task, name="new_task"),
    path("edit-task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('task-duedate-reminder/', views.task_duedate_reminder, name='task_duedate_reminder')
]