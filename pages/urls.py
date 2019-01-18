from django.urls import path

from .views import SalaryListView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('salary/', SalaryListView.as_view(), name='salary-list')
]