from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
# parent_router
router.register('', views.BlogViewSet, basename='blogs')

# child_router = routers.NestedSimpleRouter(parent_router, parent_prefix, lookup=parent_domain)
comments_router = routers.NestedSimpleRouter(router, '', lookup='')
comments_router.register('comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
]