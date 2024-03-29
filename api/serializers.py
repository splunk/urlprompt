from rest_framework import serializers
from core.models import Prompt, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username"]

class PromptSerializer(serializers.HyperlinkedModelSerializer):

    created_by = CustomUserSerializer(required=False)

    class Meta:
        model = Prompt
        fields = ["id", "created_at", "status", "schema", "url", "created_by", "response"]
        read_only_fields = ['id', 'created_at', 'created_by', 'modified_at', 'status', 'url']

class PromptResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ["response"]
        extra_kwargs = {'response': {'required': True}}
