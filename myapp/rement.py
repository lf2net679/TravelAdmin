from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Rement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rements')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.content[:50]}"

# 您可以根据需要添加更多的模型或函数