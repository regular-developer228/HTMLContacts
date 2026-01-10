from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=50),
    phone = models.CharField(max_length=15),
    mail = models.EmailField(max_length=50),
    photo = models.ImageField(
        upload_to = "contact_photo/",
        default = "default.png",
        blank = True,
        null = True
    )

    def __str__(self):
        return f"{self.name} {self.phone} {self.mail}"
