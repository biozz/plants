import datetime as dt

from django.shortcuts import get_object_or_404, render
from django.views import View, generic

from .models import Plant


def _is_between_dates(ref: dt.date, start, end):
    if start and end:
        when1 = dt.date(ref.year, start.month, start.day)
        when2 = dt.date(ref.year, end.month, end.day)
        if when1 <= ref <= when2:
            return True
    return False


class IndexView(View):
    template_name = "plants/index.html"
    context_object_name = "plants"

    def get(self, request):
        plants = Plant.objects.all()
        blooming = []
        soon = []
        other = []
        for p in plants:
            today = dt.date.today()
            if p.until and p.until > 0:
                soon.append(p)
                continue
            if _is_between_dates(today, p.bloom_start, p.bloom_end):
                blooming.append(p)
            if _is_between_dates(today, p.collect_start, p.collect_end):
                soon.append(p)
            other.append(p)
        ctx = {"blooming": blooming, "soon": soon, "other": other}
        return render(request, "plants/index.html", ctx)


class AllPlants(generic.ListView):
    template_name = "plants/all.html"
    model = Plant
    context_object_name = "plants"


class DetailView(generic.DetailView):
    model = Plant
    template_name = "plants/detail.html"
