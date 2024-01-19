from django.db import models

# Basically defines database columns

class Collection(models.Model):
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, related_name = '+')
    
class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()
    

class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)

    # one to many relation
    Collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    #  many to many relation
    promotions = models.ManyToManyField(Promotion)



class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER = 'S'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_SILVER, 'Silver'),
    ]
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 254, unique = True)
    phone = models.IntegerField(max_length = 10)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)

class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'

    PAYMENT_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now = True)
    payment_status = models.CharField(max_length = 1, choices = PAYMENT_CHOICES, default = PENDING )

    # one to many relationship with foreign key
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)

class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)

    # one to many relationship with foreign key

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

