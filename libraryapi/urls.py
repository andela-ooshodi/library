from django.conf.urls import url, include
from rest_framework import routers

from libraryapi.views import CategoryViewSet, BookViewSet

# register our v1 api URL pattern
v1_router = routers.DefaultRouter()
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'books', BookViewSet)

urlpatterns = [
    url(r'^v1/', include(v1_router.urls)),
]
