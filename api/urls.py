from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
   openapi.Info(
      title="URLP API",
      default_version='v1',
      description="API documentation for URLP Server.",
      contact=openapi.Contact(email="fdse@splunk.com")
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('api/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
