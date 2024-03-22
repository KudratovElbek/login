from django.db import models

# Create your models here.

class Cars(models.Model):
    car_name = models.CharField(max_length=255, unique=True, verbose_name='Car name')
    car_desc = models.TextField( verbose_name='car characteristics')
    car_image = models.ImageField(upload_to='images/cars/', verbose_name='Car image')



    def __str__(self):
        return self.car_name
    

    class Meta:
        verbose_name = 'Cars'
        verbose_name_plural = 'Cars'
        ordering = ['id']
        db_table = 'cars'
