from django.urls import path
from .import views


app_name = "movies"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:moives_pk>/comment/', views.comment_create, name='comment'),
    path('<int:movies_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_detail'),
    path('<int:movies_pk>/likes', views.likes, name='likes'),
]
