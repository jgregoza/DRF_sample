from django.shortcuts import render

from django.views.generic import ListView

# view DRF
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView, 
    RetrieveUpdateAPIView,
)

from .models import Person

#
from .serializers import PersonSerializer


class PersonaListView(ListView):
    template_name = "persona/lista.html"
    context_object_name = "personas"

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiView(ListAPIView):  # API's Generic views
    """Searizacion"""
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonCreateView(CreateAPIView):
    
    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView):
    
    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonDeleteView(DestroyAPIView):
    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateView(UpdateAPIView): 

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetriveUpdateView(RetrieveUpdateAPIView):   # Read or update

    serializer_class = PersonSerializer
    queryset = Person.objects.all()
