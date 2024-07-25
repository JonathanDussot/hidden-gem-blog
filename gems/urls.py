from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("about/", include("about.urls"), name="about_urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('subscribe-to-newsletter/', include("newsletter.urls")),
    path("resources/", include("resources.urls"), name="resources_urls"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog_urls"),
]
