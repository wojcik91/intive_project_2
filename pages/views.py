from django.views.generic import ListView
from django.views.generic.base import TemplateView

from .models import Salary


class SalaryListView(ListView):
    model = Salary
    template_name = 'salary.html'


class HomePageView(TemplateView):
    template_name = 'home.html'