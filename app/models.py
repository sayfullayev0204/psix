from django.db import models

# Create your models here.
from django.db import models

class Guide(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Maqolalar '  
        verbose_name_plural = 'Maqolalar '

class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField()  # YouTube yoki boshqa video linki
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Videolar '
        verbose_name_plural = 'Videolar '

class Test(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Testlar '
        verbose_name_plural = 'Testlar '

class Music(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Musiqalar '
        verbose_name_plural = 'Musiqalar '
    
class Books(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Kitoblar '
        verbose_name_plural = 'Kitoblar '