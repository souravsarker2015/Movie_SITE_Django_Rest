from rest_framework import serializers
from app.models import Stream, WatchList, Review


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = "__all__"
