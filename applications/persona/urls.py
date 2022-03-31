from django.urls import path
from . import views


app_name = "persona_app"

urlpatterns = [
    path("persona/", views.PersonaListView.as_view(), name="personas"),
    path("api/persona/lista/", views.PersonListApiView.as_view(), name="api_personas"),
    path("api/persona/create/", views.PersonCreateView.as_view(), name="api_create"),
    path("api/persona/detail/<pk>/", views.PersonDetailView.as_view(), name="api_detail"),
    path("api/persona/delete/<pk>/", views.PersonDeleteView.as_view(), name="api_delete"),
    path("api/persona/update/<pk>/", views.PersonUpdateView.as_view(), name="api_update"),
    path("api/persona/edit/<pk>/", views.PersonRetriveUpdateView.as_view(), name="api_retrive_update"),
]
