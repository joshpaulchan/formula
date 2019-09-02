from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:form_id>/submit/", views.submit_form, name="submit_form"),
]

