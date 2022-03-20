from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    shop_description = models.TextField(max_length=2055)
    shop_rating = models.DecimalField(max_digits=2, decimal_places=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    product_description = models.TextField(max_length=2055)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Review(models.Model):
    rank = models.DecimalField(max_digits=2, decimal_places=1)
    content = models.TextField(max_length=2055)
    photo = models.CharField(max_length=2048)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Connection(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    content = models.TextField(max_length=2055)
    date_time = models.DateTimeField(auto_now_add=True)
    from_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    connection_id = models.ForeignKey(Connection, on_delete=models.CASCADE)

class Question(models.Model):
    content = models.TextField(max_length=2055)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(max_length=2055)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
