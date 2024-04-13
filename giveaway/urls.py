from . import views
from django.urls import path

urlpatterns = [
    path("", views.giveaway_form, name="giveaway_form"),
]
