"""
URL configuration for advanced_features_and_security project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from django.urls import path, include # pyright: ignore[reportMissingModuleSource]


from django.conf import settings # pyright: ignore[reportMissingModuleSource]
from django.conf.urls.static import static # pyright: ignore[reportMissingModuleSource]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),
            # ... your urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
