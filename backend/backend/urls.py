from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('parser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('openapi-schema/', get_schema_view(
        title="Covid info",
        description="statistics of information for 2020 according to coronavirus cases and currency exchange rate "
                    "changes",
        version="1.0.0",
        public=True,
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    )),
]
