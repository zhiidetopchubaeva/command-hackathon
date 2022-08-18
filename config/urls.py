from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf.urls.static import static
from django.conf import settings
import cinema
import pywebio
from config.settings import STATIC_ROOT


schema_view = get_schema_view(
    openapi.Info(
        title="Cinema API",
        description="...",
        default_version="v1",
    ),
    public=True
)


# from chat.main import main
# from django.urls import path
# from pywebio.platform.django import webio_view

# # `task_func` is PyWebIO task function
# import asyncio
# webio_view_func = webio_view(
#     # lambda *args, **kwargs: asyncio.run(main(*args, **kwargs))
# ) 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # path('anime/', include('cinema.urls')),
    path('docs/', schema_view.with_ui("swagger")),
    path('', include('cinema.urls')),
    # path('chat/', webio_view_func)

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# pywebio.platform.django.webio_view(cinema, cdn = True , session_expire_seconds = None , allow_origins = None, session_cleanup_interval = None , check_origin = None )

