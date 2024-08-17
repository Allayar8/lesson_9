from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    category_name = models.CharField(max_length=255,verbose_name='Названия Категорий',)
    slug = models.SlugField(verbose_name='Слаг категорий',max_length=255,)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'
        
    def __str__(self) -> str:
        return self.category_name
    
class Blogs(models.Model):
    avtor = models.ForeignKey(User,on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    title = models.CharField(max_length=255,verbose_name='Названия поста:',)
    text = models.TextField(verbose_name='Текст поста:',)
    image1 = models.ImageField(verbose_name='1 Картинка для поста(не обьязательно)',blank=True,null=True,)
    image2 = models.ImageField(verbose_name='2 Картинка для поста(не обьязательно)',blank=True,null=True,)
    image3 = models.ImageField(verbose_name='3 Картинка для поста(не обьязательно)',blank=True,null=True,)
    pub_date = models.DateTimeField(auto_now_add=True,)
    
    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        
    def __str__(self) -> str:
        return self.title
    
    