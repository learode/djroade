from .models import Blog
from .serializers import BlogSerializer

from rest_framework import generics

# Create your views here.
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


blog_list   = BlogList.as_view()
blog_detail = BlogDetail.as_view()
