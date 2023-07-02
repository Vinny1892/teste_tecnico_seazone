from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from announcement.serializers import AnnouncementSerializer
from immobile.models import Immobile


class ImmobileSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(
        validators=[UniqueValidator(queryset=Immobile.objects.all())]
    )
    announcement = AnnouncementSerializer(many=True,required=False)


    def create(self, validated_data):
        code = validated_data.get("code")
        if Immobile.objects.filter(code=code).exists():
            raise serializers.ValidationError("The code must be unique.")
        # return Immobile.objects.create(**validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        return instance

    class Meta:
        model = Immobile
        fields = "__all__"
