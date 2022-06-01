from django.db import models
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    servidor = models.ForeignKey(
            'auth.User',
            on_delete = models.CASCADE
    )
    nombre_autor = models.CharField(max_length=50)
    ingredientes = models.TextField()
    pasos = models.TextField()

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

# Create your models here.
