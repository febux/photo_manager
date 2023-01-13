from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView, get_object_or_404, ListAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import PhotoFilter
from .models import Photo
from .serializers import PhotoSerializerList, PhotoSerializer


class PhotoViewList(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializerList
    name = 'photo-list'
    filter_backends = [DjangoFilterBackend]
    filterset_class = PhotoFilter


class PhotoView(RetrieveModelMixin, GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    name = 'photo'

    def get(self, request, pk, *args, **kwargs):
        queryset = Photo.objects.all()
        photo = get_object_or_404(queryset, pk=pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)


class PhotoViewCreate(CreateModelMixin, GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
