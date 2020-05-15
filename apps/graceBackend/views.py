from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.graceBackend.models import Entry
from .serializers import EntrySerializer


class CreateEntry(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Entry.objects.all()
        return queryset
    serializer_class = EntrySerializer

class PublicEntries(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Entry.objects.all().filter(is_public=True)
        return queryset

    serializer_class = EntrySerializer

class PublicEntriesDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Entry.objects.all().filter(is_public=True)
        return queryset

    serializer_class = EntrySerializer