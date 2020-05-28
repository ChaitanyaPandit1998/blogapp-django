from django.urls import path
from . import views
from .views import BlogCreateView,BlogUpdateView,BlogDeleteView

app_name='blog'
urlpatterns = [
  path('',views.index,name='index'),
  path('post/<int:blog_id>/',views.detail,name='detail'),
  path('post/new/',BlogCreateView.as_view(),name='add'),
  path('post/<int:pk>/edit/',BlogUpdateView.as_view(),name='edit'),
  path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='delete'),
]