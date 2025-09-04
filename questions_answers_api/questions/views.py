from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from answers.serializers import AnswerReadSerializer, AnswerCreateSerializer

from .models import Question
from .serializers import (QuestionDetailSerializer,
                          QuestionListSerializer, QuestionCreateSerializer)


class QuestionViewSet(viewsets.ModelViewSet):

    def get_queryset(self) -> QuerySet[Question]:
        # Для детального просмотра предзагружаем ответы
        if self.action == 'retrieve':
            return Question.objects.prefetch_related('answers')
        return Question.objects.all()

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        if self.action == 'create':
            return QuestionCreateSerializer
        return QuestionListSerializer

    def update(self, request, *args, **kwargs) -> MethodNotAllowed:
        return MethodNotAllowed('PUT')

    def partial_update(self, request, *args, **kwargs) -> MethodNotAllowed:
        return MethodNotAllowed('PATCH')

    # Понять добавляем один объект (ответ) или коллекцию (ответы).
    # Во втором случае detail=False
    @action(detail=True, methods=['post'], url_path='answers')
    def add_answer(self, request, pk) -> Response:
        """
        Создание ответа для конкретного вопроса
        POST /questions/{id}/answers/
        """
        question = get_object_or_404(Question, id=pk)
        answer_text = request.data.copy()
        serializator = AnswerCreateSerializer(data=answer_text)
        if serializator.is_valid():
            serializator.save(question=question)
            return Response(serializator.data, status.HTTP_201_CREATED)
        return Response(serializator.errors, status.HTTP_400_BAD_REQUEST)
