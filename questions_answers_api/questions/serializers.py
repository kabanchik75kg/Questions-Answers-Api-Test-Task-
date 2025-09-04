from rest_framework import serializers

from core.validators import validate_not_empty
from .models import Question
from answers.serializers import AnswerReadSerializer


# Сериализатор для создания вопроса (требуется валидация).
class QuestionCreateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(validators=[validate_not_empty])

    class Meta:
        model = Question
        fields = ('text', )


# Сериализатор для чтения вопроса.
class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerReadSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'created_at', 'answers')


# Сериализатор для чтения списка вопросов.
class QuestionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'text', 'created_at')
