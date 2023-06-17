from .views import blog_detail, blog_list

from django.urls import path

urlpatterns = [
    path('', blog_list),
    path('<int:pk>', blog_detail, name='blog-detail'),
]
