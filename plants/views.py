import datetime as dt

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Plant


def _is_between_dates(ref: dt.date, start, end):
    if start and end:
        when1 = dt.date(ref.year, start.month, start.day)
        when2 = dt.date(ref.year, end.month, end.day)
        if when1 <= ref <= when2:
            return True
    return False


class PlantsRecent(generic.ListView):
    template_name = "plants/index.html"
    model = Plant
    context_object_name = "plants"

    def get_queryset(self):
        return Plant.objects.order_by("-created_at")[:5]


class PlantsAll(generic.ListView):
    template_name = "plants/all.html"
    model = Plant
    context_object_name = "plants"
    paginate_by = 5


@method_decorator(login_required, name="dispatch")
class PlantDetail(generic.DetailView):
    model = Plant
    template_name = "plants/detail.html"


@method_decorator(login_required, name="dispatch")
class PlantCreate(generic.CreateView):
    template_name = "plants/create.html"
    model = Plant
    fields = ["name", "name_alt", "name_en", "thumbnail"]
    success_url = reverse_lazy("index")


@method_decorator(login_required, name="dispatch")
class PlantUpdate(generic.UpdateView):
    template_name = "plants/update.html"
    model = Plant
    fields = ["name", "name_alt", "name_en", "thumbnail"]


@method_decorator(login_required, name="dispatch")
class PlantDelete(generic.DeleteView):
    model = Plant


@method_decorator(login_required, name="dispatch")
class PlantsSearch(generic.ListView):
    template_name = "plants/search_results.html"
    model = Plant
    context_object_name = "plants"

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        return Plant.objects.filter(
            Q(name__icontains=q) | Q(name_en__icontains=q) | Q(name_alt__icontains=q)
        )[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        return context
