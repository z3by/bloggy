from django.contrib import admin
from django.urls import include ,path
from django.contrib.sitemaps.views import sitemap
from django.shortcuts import redirect

from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

def index_page(request):
    return redirect('blog/')


urlpatterns = [
    path('', index_page),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
