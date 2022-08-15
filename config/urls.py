from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Shop 21 API",
        description="...",
        default_version="v1",
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('cinema/', include('cinema.urls')),
    path('docs/', schema_view.with_ui("swagger"))
]
