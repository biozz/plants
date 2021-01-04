from django.contrib import admin
from django.urls import include, path

from plants import views as plants_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("plants/", include("plants.urls")),
    path("", plants_views.IndexView.as_view(), name="index"),
]
