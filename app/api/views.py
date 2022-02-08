from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from app.api.permission import IsReviewUserOrReadOnly, IsAdminOrReadOnly
from app.models import (Stream,
                        WatchList,
                        Review)
from app.api.serializers import (StreamSerializer,
                                 WatchListSerializer,
                                 ReviewSerializer)


@api_view(['POST'])
def review_create(request, pk):
    if request.method == "POST":
        watchlist = WatchList.objects.get(id=pk)
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            review_user = request.user
            review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
            if review_queryset.exists():
                raise ValidationError("You already reviewed")

            if watchlist.avg_rating == 0:
                watchlist.avg_rating = serializer.validated_data['rating']
            else:
                watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2
            watchlist.num_rating = watchlist.num_rating + 1
            watchlist.save()
            serializer.save(watchlist=watchlist, review_user=review_user)
            return Response(serializer.data)

        else:
            content = {"error": "data is not valid"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class WatchListAV(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class WatchListDetailAV(APIView):
    def get(self, request, pk):
        watchlist = WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    def put(self, request, pk):
        watchlist = WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        WatchList.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)


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


@api_view(['GET', 'PUT', 'DELETE'])
def stream_details(request, pk):
    if request.method == "GET":
        stream = Stream.objects.get(id=pk)
        serializer = StreamSerializer(stream)
        return Response(serializer.data)

    if request.method == "PUT":
        stream = Stream.objects.get(pk=pk)
        serializer = StreamSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == "DELETE":
        Stream.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)
