from django.urls import path

from . import views


urlpatterns = [
    path("", views.MenView.as_view()),
    path("<int:pk>/", views.MenDetailView.as_view(), name="men"),
]