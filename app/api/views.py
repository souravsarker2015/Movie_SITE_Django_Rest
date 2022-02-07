from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Stream, WatchList, Review
from app.api.serializers import StreamSerializer


@api_view(['GET', 'POST'])
def stream_list(request):
    if request.method == "GET":
        stream = Stream.objects.all()
        serializer = StreamSerializer(stream, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            content = {"error": "data is not valid"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
