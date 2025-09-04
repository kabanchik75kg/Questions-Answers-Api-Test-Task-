from rest_framework import viewsets

from .models import Answer
from .serializers import AnswerReadSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """ViewSet для ответов, поддерживающий только необходимые методы"""

    queryset = Answer.objects.all()
    serializer_class = AnswerReadSerializer
    http_method_names = ('get', 'delete', 'head', 'options')
