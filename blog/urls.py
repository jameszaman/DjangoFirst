from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView #class we created.

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'), # need to convert the class as a view
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('about/', views.about, name='blog-about'),
]