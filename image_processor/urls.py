"""
URL configuration for image_processor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from images.views import ImageViewSet
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Image Processor",
        default_version='v1',
        description="This API allows users to upload an image and process it asynchronously. Processing includes operations such as applying filters or transformations (in this case converting to grayscale) to the uploaded image.",
        contact=openapi.Contact(email="nicolashurtado0712@gmail.com"),
        license=openapi.License(name="Nicolas Hurtado C"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


image_list = ImageViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

image_detail = ImageViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/images/', image_list, name='image-list'),
    path('api/images/<int:pk>/', image_detail, name='image-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
