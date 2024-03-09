from django.db import models
from django.contrib.auth.models import AbstractUser


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', blank=True,null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True,null=True)
    phone_number = models.CharField(max_length=255,null=True,blank=True)




    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Product(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Sub_category', on_delete=models.PROTECT)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, blank=True)
    color = models.ManyToManyField(to='Color', blank=True)
    photos = models.ManyToManyField(to='Image')
    quantity = models.IntegerField(default=0)
    features = models.TextField()
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    old_cost = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    discount_percent = models.IntegerField(default=0)
    is_banner = models.BooleanField(default=False)
    is_delivery = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    size_category = models.ForeignKey('Size_category', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateField(auto_now=True)


class Sub_category(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateField(auto_now=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)



class Color(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='color_photo/')



class Image(models.Model):
    img = models.ImageField(upload_to='product_photo/')


class Size_category(models.Model):
    name = models.CharField(max_length=25)


class Card(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    product = models.ManyToManyField('Product')
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

class Saved(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    product = models.ManyToManyField('Product')


class Office(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    pass_number = models.CharField(max_length=20)
    is_delivery = models.BooleanField(default=False)
    extra_phone_number = models.CharField(max_length=255, null=True, blank=True)
    payment_type = models.BooleanField(default=True)
    office = models.ForeignKey(to=Region,on_delete=models.CASCADE)
    lat = models.FloatField()
    lot = models.FloatField()