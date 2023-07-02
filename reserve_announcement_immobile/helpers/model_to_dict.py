from django.db.models import Model
from rest_framework.serializers import ModelSerializer


def response_to_data_input(
    model: Model, serializer: ModelSerializer, response_data: dict
) -> dict:
    data = serializer(model).data
    common_keys = set(response_data.keys()) & set(data.keys())
    model_dict = {key: data[key] for key in common_keys}
    return model_dict


def model_to_data_input(model: Model, serializer: ModelSerializer) -> dict:
    data = serializer(model).data
    return data
