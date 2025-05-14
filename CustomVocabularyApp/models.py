from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    word = models.CharField(max_length=100, unique=True)  # ✅ For short text, like a single word
    meaning = models.TextField()  # ✅ For longer text, like multiple sentences
