from django.db import models


# Create your models here.
class Item(models.Model):
    
    product_id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=100, blank=False)
    isDigital = models.BooleanField()
    # color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    color = models.CharField(max_length=50, blank=False)
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.sku == '':
            raise ValidationError('Empty stock keeping unit')
        if self.title == '':
            raise ValidationError('Empty title error')     

   

   
    

    class Meta:
        ordering = ['product_id']
