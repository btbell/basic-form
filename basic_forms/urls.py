from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.hello, name='hello'),
    path('posts', views.ListPosts.as_view(), name='posts'),
    path('post/newccc/', views.post_new, name='post_new'),
]