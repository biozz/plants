from django.contrib import admin
from django.urls import include, path

from plants import views as plants_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("plants/", include("plants.urls")),
    path("", plants_views.PlantsRecent.as_view(), name="index"),
]
