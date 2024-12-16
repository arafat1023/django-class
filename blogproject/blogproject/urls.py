from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Admin customizations
admin.site.site_header = "Blog Platform Administration"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to the Blog Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include the blog app URLs
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
