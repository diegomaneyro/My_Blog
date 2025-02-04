from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# Categorias
class Category(models.Model):
    name = models.CharField(max_length=255)  # Cambié False a 255
    image = models.ImageField(blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=40)  # URL amigable
    featured = models.BooleanField(default=False)  # Al crear una categoria por defecto no es destacada
    created = models.DateTimeField(auto_now_add=True)  # Conocer la fecha en que se registró la categoria
    updated = models.DateTimeField(auto_now=True)  # Conocer la fecha de actualización de una categoria
    status = models.BooleanField(default=True)  # Al registrarla estar activa

    def __str__(self):
        return self.name

    # clase de metadatos
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Articulo
class Article(models.Model):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField()
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Cambié user_id a user
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)  # Conocer la fecha en que se registró el artículo
    updated = models.DateTimeField(auto_now=True)  # Conocer la fecha de actualización de un artículo
    status = models.BooleanField(default=True)  # Al registrarla estar activa

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

# Calificaciones
class Rating(models.Model):
    value = models.FloatField()  # Asignar una calificación
    description = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Cambié article_id a article
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Cambié user_id a user
    created = models.DateTimeField(auto_now_add=True)  # Conocer la fecha en que se registró la calificación
    status = models.BooleanField(default=True)  # Al registrarla estar activa

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
