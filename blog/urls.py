from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('new_comment/<int:post_id>/', views.new_comment, name='new_comment'),
    path('about_us/', views.about_us, name='about_us')
]