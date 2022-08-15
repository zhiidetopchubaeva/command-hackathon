"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf.urls.static import static
from django.conf import settings

from config.settings import STATIC_ROOT


schema_view = get_schema_view(
    openapi.Info(
        title="Cinema API",
        description="...",
        default_version="v1",
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # path('anime/', include('cinema.urls')),
    path('docs/', schema_view.with_ui("swagger")),
    path('', include('cinema.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

