from django.urls import path

from . import views

app_name = "plants"

urlpatterns = [
    path("all/", views.PlantsAll.as_view(), name="all"),
    path("my/", views.PlantsMy.as_view(), name="my"),
    path("<int:pk>/", views.PlantDetail.as_view(), name="detail"),
    path("create/", views.PlantCreate.as_view(), name="create"),
    path("<int:pk>/update/", views.PlantUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", views.PlantDelete.as_view(), name="delete"),
    path("search/", views.PlantsSearch.as_view(), name="search"),
]
