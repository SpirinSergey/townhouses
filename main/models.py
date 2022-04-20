from django.db import models


class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='images/')


class Listing(models.Model):
    FLOOR = models.CharField(null=True, max_length=20)
    UNIT_FORM = models.CharField(null=True, max_length=20)
    UNIT_TYPE = models.CharField(null=True, max_length=300)
    BEDROOMS = models.CharField(null=True, max_length=5)
    BATHROOMS = models.CharField(null=True, max_length=5)
    UNIT = models.CharField(null=True, max_length=20)
    INTERIOR = models.CharField(null=True, max_length=50)
    TERRACE = models.CharField(null=True, max_length=50)
    TOTAL = models.CharField(null=True, max_length=50)
    PRICE = models.CharField(null=True, max_length=50)
    FLOOR_PLANE = models.FileField(upload_to='floor_plane/', blank=True)


class FeedBack(models.Model):
    user_type_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    first_name = models.CharField(max_length=150, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Last name')
    phone = models.CharField(max_length=150, blank=True, verbose_name='Phone')
    email = models.EmailField(blank=True, verbose_name='Email')
    agent_type = models.CharField(max_length=150,  blank=True, choices=user_type_choices, verbose_name='Is a realtor')
    message = models.TextField(blank=True, verbose_name='message')
    date_creation = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date creation')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Feedbacks'


class BookPoint(models.Model):
    user_type_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    time_choices = (
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
    )

    first_name = models.CharField(max_length=150, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Last name')
    phone = models.CharField(max_length=150, blank=True, verbose_name='Phone')
    email = models.EmailField(blank=True, verbose_name='Email')
    agent_type = models.CharField(max_length=150,  blank=True, choices=user_type_choices, verbose_name='Is a realtor')
    message = models.TextField(blank=True, verbose_name='message')
    date = models.CharField(max_length=50, blank=True, verbose_name='Date and time')
    date_creation = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date creation')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Book an appointments'
