from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    alternative = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='contacts_images/', blank=True, null=True)

    def __str__(self):
        return self.name