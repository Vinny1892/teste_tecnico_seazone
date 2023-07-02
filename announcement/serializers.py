from rest_framework import serializers

from announcement.models import Announcement
from immobile.models import Immobile


class AnnouncementSerializer(serializers.ModelSerializer):
    immobile_id = serializers.PrimaryKeyRelatedField(
        queryset=Immobile.objects.all(),
        source='immobile',
        write_only=True
    )

    class Meta:
        model = Announcement
        fields = "__all__"
        depth = 1
