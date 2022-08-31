from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('Category image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Welcome(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_welcome', blank=True)
    name = models.TextField('Name')
    img = models.ImageField('Img name', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Welcome'
        verbose_name_plural = 'Welcome'

class OurTeam(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_ourteam', blank=True)
    name = models.TextField('Name')
    img = models.ImageField('Img name', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OurTeam'
        verbose_name_plural = 'OurTeams'

class OurWork(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_work', blank=True)
    name = models.CharField('Name', max_length=30)
    about = models.TextField('About')
    img = models.ImageField('Img name', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OurWork'
        verbose_name_plural = 'OurWorks'