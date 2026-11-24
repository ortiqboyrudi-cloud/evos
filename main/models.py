from django.db import models

class Taom(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Taom nomi")
    tavsifi = models.TextField(blank=True, null=True, verbose_name="Tavsifi")
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi (so'm)")
    rasm_url = models.URLField(blank=True, null=True, verbose_name="Rasm havolasi (URL)")

    def __str__(self):
        return self.nomi

class Banner(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Banner nomi")
    rasm_url = models.URLField(verbose_name="Rasm havolasi (URL)")

    def __str__(self):
        return self.nomi