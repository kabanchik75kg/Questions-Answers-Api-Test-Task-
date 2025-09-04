from django.db import models

from core.models import CreatedModel
from questions.models import Question


class Answer(CreatedModel):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос'
    )
    user_id = models.UUIDField(verbose_name='ID пользователя')
    text = models.TextField(verbose_name='Текст ответа')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'User:{self.user_id}. Answer_text: {self.text}'
