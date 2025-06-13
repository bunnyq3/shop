from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25,unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class item(models.Model):
    name = models.CharField(max_length=25,unique=True)
    price = models.DecimalField()
    discount_time = models.CharField(max_length=25,null=False)
    discount_price = models.DecimalField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    






