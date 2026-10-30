from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from home.sitemaps import StaticViewSitemap
from home.views_seo import robots_txt, llms_txt


# Sitemap configuration
sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('careers/', include('careers.urls')),

    # SEO URLs
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('llms.txt', llms_txt, name='llms_txt'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )