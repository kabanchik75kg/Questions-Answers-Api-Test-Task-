from rest_framework import serializers

from core.validators import validate_not_empty
from .models import Answer


class AnswerCreateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(validators=[validate_not_empty])

    class Meta:
        model = Answer
        fields = ('text', 'user_id')


class AnswerReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'text', 'user_id', 'created_at')
