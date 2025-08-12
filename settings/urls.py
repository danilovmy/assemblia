from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views import generic


handler404 = "settings.views.handler404"
handler500 = "settings.views.handler500"

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('schema.yaml', generic.RedirectView.as_view(url='/media/schema.yaml'), name='schema.yaml'),
    # path('docs/', generic.TemplateView.as_view(template_name='schema.html'), name='docs'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)