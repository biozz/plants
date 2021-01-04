from django.urls import path

from . import views

app_name = "plants"

urlpatterns = [
    path("all/", views.AllPlants.as_view(), name="all"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
