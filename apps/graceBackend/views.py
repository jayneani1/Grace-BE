from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.graceBackend.models import Entry
from .serializers import EntrySerializer

class EntryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Entry.objects.all()
        return queryset

    serializer_class = EntrySerializer

    def create(self, request, *args, **kwargs):
        print request.data
       # if request.user.is_anonymous:
        #    raise PermissionDenied(
         #       "Only logged in users with accounts can enter")
       # return super().create(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        entry = Entry.objects.get(pk=self.kwargs["pk"])
        if not request.user == entry.owner:
            raise PermissionDenied(
                "You have no permissions to delete this")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        entry = Entry.objects.get(pk=self.kwargs["pk"])
        if not request.user == entry.owner:
            raise PermissionDenied("Only the author can edit this")
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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