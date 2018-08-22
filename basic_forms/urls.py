from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello', views.hello, name='hello'),
    path('posts', views.ListPosts.as_view(), name='posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]