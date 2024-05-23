
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import urls as home_urls
from accounts import urls as account_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('accounts/', include(account_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
