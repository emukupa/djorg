from rest_framework import serializers, viewsets
from . models import Bookmark


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['name', 'url']

    def create(self, validated_data):
        # import pdb; pdb.set_trace() # for debugging
        user = self.context['request'].user
        bookmark_user = Bookmark.objects.create(user=user, **validated_data)
        return bookmark_user


class BookmarkViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
