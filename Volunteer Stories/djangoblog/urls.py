from rest_framework import routers
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import UserModelViewSet, ImageModelViewSet, VolunteerModelViewSet
from blog.views import CategoryModelViewSet, SubCategoryModelViewSet, PostModelViewSet

router = routers.DefaultRouter()
router.register(r'user', UserModelViewSet, basename='user')
router.register(r"category", CategoryModelViewSet, basename="category")
router.register(r"sub-category", SubCategoryModelViewSet, basename="sub_category")
router.register(r"post", PostModelViewSet, basename="post")
router.register(r"image", ImageModelViewSet, basename="image")
router.register(r"volunteer", VolunteerModelViewSet, basename="volunteer")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path("auth/", include("accounts.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:  # pragma:no cover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
