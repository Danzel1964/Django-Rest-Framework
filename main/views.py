from django.shortcuts import get_object_or_404
# from django.shortcuts import render
from main.models import Nate
from main.serializers import NoteSerializer
from rest_framework.viewsets import ModelViewSet


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    
    
    def get_object(self):
        return get_object_or_404(Nate, pk=self.request.query_params.get('id'))
    
    
    def get_queryset(self):
        return Nate.objects.all()
        
    
