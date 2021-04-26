from rest_framework import serializers
from core.models import Prompt


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id','schema', 'response', 'created_at', 'created_by', 'modified_at', 'status']
        read_only_fields = ['id', 'created_at', 'created_by', 'modified_at', 'status']