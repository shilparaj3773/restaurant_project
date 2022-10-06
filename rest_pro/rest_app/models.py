from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):

    is_chef = models.BooleanField(default=False)
    is_waiter = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    Address = models.TextField(max_length=100)
    Qualification =models.CharField(max_length=100)
    Experience = models.IntegerField()
    specialisation = models.CharField(max_length=100)

class waiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    Address = models.TextField(max_length=100)
    Qualification =models.CharField(max_length=100)
    Experience = models.IntegerField()

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    Address = models.TextField(max_length=100)

class food(models.Model):
    food_name = models.CharField(max_length=100)
    food_price =models.IntegerField()
    food_type = models.CharField(max_length=100)
    food_image = models.FileField(upload_to="foodimage")

class payment(models.Model):
    custom = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    food_name = models.CharField(max_length=100)
    food_price =models.IntegerField()
    food_type = models.CharField(max_length=100)
    food_image = models.FileField(upload_to="food")
    card_number = models.IntegerField()
    cvv = models.IntegerField()
    date = models.DateField()
    order_status = models.IntegerField(default=False)
    delivery_status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.food_name

