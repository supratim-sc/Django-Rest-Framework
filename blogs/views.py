from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Blog, Comment
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination
from api.serializers import BlogSerializer, CommentSerializer

# Create your views here.
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomLimitOffsetPagination

class CommentViewSet(ModelViewSet):
    # As we need to filter comments based on the blog_id,
    # so, we used the 'get_query_set method so tht we can have access to the 'self' parameter
    # Now, as we have the access the 'self' parameter, we can fetch the 'id' of the 'blog' 
    # using 'self.kwargs[]'. Now, we need the 'id' to filter. While registering the 'blogs' route,
    # we specified the perfix as '' empty string. So, while filtering the 'blog_id' we need to 
    # use "self.kwargs['_pk']". Empty srting then '_pk'. if we have used perfix as 'blogs' for the
    # 'blogs' route, then our pk will be 'blogs_pk' from the url.
    def get_queryset(self):
        return Comment.objects.filter(blog_id=self.kwargs['_pk'])
    serializer_class = CommentSerializer