from rest_framework import serializers


def validate_not_empty(message: str) -> str:
    """Проверяет, что строка не пустая и не состоит только из пробелов."""

    if isinstance(message, str) and not message.strip():
        raise serializers.ValidationError(
            'Поле не может быть пустым или состоять только из пробелов!!!'
        )
    return message.strip()
