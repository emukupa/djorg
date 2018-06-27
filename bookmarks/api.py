from rest_framework import serializers, viewsets
from . models import Bookmark


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['name', 'url', 'category', 'description']


class BookmarkViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
