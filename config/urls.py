from django.contrib import admin
from django.urls import include ,path

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
