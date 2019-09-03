from django.urls import path

from . import views

urlpatterns = [path("<int:form_id>/submit/", views.submit_form, name="submit_form")]

