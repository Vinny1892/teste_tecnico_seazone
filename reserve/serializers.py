from rest_framework import serializers

from announcement.models import Announcement
from reserve.models import Reserve


class ReserveSerializer(serializers.ModelSerializer):
    announcement_id = serializers.PrimaryKeyRelatedField(
        queryset=Announcement.objects.all(),
        source='announcement',
        write_only=True
    )

    def validate(self, data_validate):
        if data_validate['check_in'] > data_validate['check_out']:
            raise serializers.ValidationError("The checkin date is after checkout date")
        return data_validate


    class Meta:
        model = Reserve
        fields = "__all__"
        depth = 1


