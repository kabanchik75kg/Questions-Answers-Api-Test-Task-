from django.db import models
from core.models import CreatedModel


class Question(CreatedModel):
    text = models.TextField()

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text
