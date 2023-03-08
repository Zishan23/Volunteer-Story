from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from blog.models import PostModel, CategoryModel, SubCategoryModel
from blog.serializers import PostModelSerializer, CategoryModelSerializer, SubCategoryModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryModelSerializer.List
        return CategoryModelSerializer.Write


class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategoryModel.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = {
        'category': ['exact'],
    }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubCategoryModelSerializer.List
        return SubCategoryModelSerializer.Write


class PostModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = {
        'featured': ['exact'],
        'category': ['exact'],
        'sub_category': ['exact'],
        'author': ['exact'],
        'is_published': ['exact'],
        'accepted_by': ['exact'],
    }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostModelSerializer.List
        return PostModelSerializer.Write

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_admin:
            return PostModel.objects.all()
        return PostModel.objects.filter(author=self.request.user)

