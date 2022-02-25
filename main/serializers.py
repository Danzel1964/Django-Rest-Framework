# используется для инфы с JSON и наоборот

from rest_framework import serializers
from main.models import Nate


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nate 
        fields = ('title', 'content', 'created_at' ,'updated_ar')