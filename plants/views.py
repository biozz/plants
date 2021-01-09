from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import get_messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse
from django.views import generic

from .models import Plant


class PlantsRecent(generic.ListView):
    template_name = "plants/index.html"
    model = Plant
    context_object_name = "plants"

    def get_queryset(self):
        return Plant.objects.order_by("-created_at")[:5]


class PlantsAll(generic.ListView):
    template_name = "plants/list.html"
    model = Plant
    context_object_name = "plants"
    ordering = "name"
    paginate_by = 5
    extra_context = {"title": "Все растения"}


class PlantsMy(LoginRequiredMixin, generic.ListView):
    template_name = "plants/list.html"
    model = Plant
    context_object_name = "plants"
    paginate_by = 5
    extra_context = {"title": "Мои растения"}

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user).order_by("name")


class PlantDetail(LoginRequiredMixin, generic.DetailView):
    model = Plant
    template_name = "plants/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_messages = get_messages(self.request)
        context["success_messages"] = [
            m for m in all_messages if m.level == messages.SUCCESS
        ]
        return context


class PlantCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "plants/create.html"
    model = Plant
    fields = ["name", "name_lat", "name_en", "name_alt", "thumbnail"]
    success_message = "Растение создано!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("plants:detail", kwargs={"pk": self.object.pk})


class PlantUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name = "plants/update.html"
    model = Plant
    fields = ["name", "name_alt", "name_en", "thumbnail"]


class PlantDelete(LoginRequiredMixin, generic.DeleteView):
    model = Plant


class PlantsSearch(LoginRequiredMixin, generic.ListView):
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
