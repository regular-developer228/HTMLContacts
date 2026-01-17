from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    mail = models.EmailField(max_length=50, blank=True, null=True)
    photo = models.ImageField(
        upload_to = "contact_photo/",
        default = "default.png",
        blank = True,
        null = True
    )

    def __str__(self):
        return f"{self.name} {self.phone} {self.mail}"
