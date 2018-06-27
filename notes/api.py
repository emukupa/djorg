from rest_framework import serializers, viewsets
from . models import Note, PersonalNote


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content']


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ['title', 'content']


class NoteViewset(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class PersonalNoteViewset(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
