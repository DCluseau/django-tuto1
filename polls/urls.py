from django.urls import include, path
from . import admin

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]