from django.db import models

# Create your models here.
class Nate(models.Model):
    title= models.CharField('Заголовок',max_length=50)
    content= models.TextField('Контент')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ar = models.DateTimeField(auto_now = True)
    
    
    def __str__(self):
        return self.title
