from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from questions.models import Question
from answers.models import Answer


class AnswerTests(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(text="Test question?")
        self.answer = Answer.objects.create(
            question=self.question,
            user_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Test answer"
        )

    def test_get_answer(self):
        url = reverse('answers-detail', args=[self.answer.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.answer.text)

    def test_delete_answer(self):
        url = reverse('answers-detail', args=[self.answer.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Answer.objects.count(), 0)

    def test_empty_answer_validation(self):
        url = reverse('questions-add-answer', args=[self.question.id])
        data = {
            'text': '   ',
            'user_id': 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
