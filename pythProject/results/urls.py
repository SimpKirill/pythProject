from django.urls import path
from . import views
from django.views.generic import ListView
from testForm.models import FormDataModel

urlpatterns = [   
    path('',ListView.as_view(queryset=FormDataModel.objects.all(),template_name="results/results.html")),
]