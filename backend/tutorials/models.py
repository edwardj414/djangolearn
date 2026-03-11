from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=10, default='📘')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Lesson(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    topic = models.ForeignKey(Topic, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()          # Markdown content
    code_example = models.TextField(blank=True)  # Default code in editor
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        unique_together = ['topic', 'slug']

    def __str__(self):
        return f"{self.topic.title} > {self.title}"
