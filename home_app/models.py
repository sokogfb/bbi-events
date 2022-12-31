from django.db import models
from django.utils.timezone import now


class gallery(models.Model):
    date = models.DateTimeField(auto_now=True, auto_created=True)
    name = models.CharField(max_length=25, verbose_name="Image Name")
    picture = models.FileField(upload_to="gallery")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'GALLERY'
        verbose_name_plural = 'GALLERY'


class passed_weddings(models.Model):
    date = models.DateTimeField(auto_now=True, auto_created=True)
    name = models.CharField(max_length=25, verbose_name="Image Name")
    bride = models.CharField(max_length=25, verbose_name="Bride's Name")
    groom = models.CharField(max_length=25, verbose_name="Groom's Name")
    picture = models.FileField(upload_to="gallery")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'PASSED WEDDING'
        verbose_name_plural = 'PASSED WEDDINGS'
