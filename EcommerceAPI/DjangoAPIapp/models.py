from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageurl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageurl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
    
    
