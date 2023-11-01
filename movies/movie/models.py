from django.db import models
from django.utils import timezone

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    fecha_estreno = models.DateField(default='1500-05-10')
    rating = models.DecimalField(decimal_places=2, max_digits=10)
    genero = models.ForeignKey(
        'movie.genero',
        on_delete=models.CASCADE,
        related_name='movie'
    )

    image = models.ImageField(
        blank=True, null=True,
        upload_to='media/products'
    )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} | '

class Genero(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} | '
    
class Comentario(models.Model):
    movie = models.ForeignKey(
        'movie.Movie',
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    usuario = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.text
    

    

