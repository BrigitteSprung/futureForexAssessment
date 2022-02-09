from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class DashboardView(generic.DetailView):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
