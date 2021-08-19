from django.db import models

from users.models import Profile


class CarCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Car Categories'


class Car(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                               related_name='cars', blank=True, null=True)
    brand = models. ForeignKey(CarCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    volume = models.FloatField()
    price = models.FloatField()
    release_date = models.DateTimeField()
    color = models.CharField(max_length=255)
    transmission = models.CharField(max_length=225)
    rul = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='cars', blank=True, null=True)
    posted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
