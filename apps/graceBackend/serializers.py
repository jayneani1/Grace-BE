from rest_framework import serializers
from apps.graceBackend.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Entry
        fields = ('id', 'title', 'owner', 'description',
                   'mood', 'created_at', 'updated_at', 'is_public' )