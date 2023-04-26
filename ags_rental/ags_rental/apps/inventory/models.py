from django.db import models
from django.core.files import File
import qrcode


class Case(models.Model):
    name = models.CharField(max_length=512)
    quantity = models.PositiveIntegerField()
    qr_code = models.ImageField(blank=True, null=True, upload_to='images/cases/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.qr_code:
            qr_code = qrcode.make(self.id)
            qr_code.save(f'images/cases/{self.id}_case_qr_code.png')
        self.qr_code = f'images/cases/{self.id}_case_qr_code.png'
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=512)
    quantity = models.PositiveIntegerField()
    qr_code = models.ImageField(blank=True, null=True, upload_to='images/devices/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.qr_code:
            qr_code = qrcode.make(self.id)
            qr_code.save(f'images/devices/{self.id}_device_qr_code.png')
        self.qr_code = f'images/devices/{self.id}_device_qr_code.png'
        super().save(*args, **kwargs)
