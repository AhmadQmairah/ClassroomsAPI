
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from api import views as views2
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('classroom/list', views2.ClassRoomView.as_view(), name='list'),
    path('classroom/detail/<int:classroom_id>', views2.DetailView.as_view(), name='detail'),
    path('classroom/create/', views2.CreateView.as_view(), name='create'),
    path('classroom/update/<int:classroom_id>', views2.UpdateView.as_view(), name='Update'),
    path('classroom/delete/<int:classroom_id>', views2.DeleteView.as_view(), name='delete'),
     path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
