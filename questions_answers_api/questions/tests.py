from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from questions.models import Question
from answers.models import Answer


class QuestionTests(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(text="Test question?")
        self.answer = Answer.objects.create(
            question=self.question,
            user_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Test answer"
        )

    def test_create_question(self):
        url = reverse('questions-list')
        data = {'text': 'New test question?'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)

    def test_get_questions_list(self):
        url = reverse('questions-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_question_detail(self):
        url = reverse('questions-detail', args=[self.question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.question.text)
        self.assertEqual(len(response.data['answers']), 1)

    def test_delete_question(self):
        url = reverse('questions-detail', args=[self.question.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.count(), 0)
        # Проверяем каскадное удаление ответов
        self.assertEqual(Answer.objects.count(), 0)

    def test_create_answer_to_question(self):
        url = reverse('questions-add-answer', args=[self.question.id])
        data = {
            'text': 'Another answer',
            'user_id': 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.question.answers.count(), 2)

    def test_empty_text_validation(self):
        url = reverse('questions-list')
        data = {'text': '   '}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
