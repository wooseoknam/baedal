from django.db import models

# Create your models here.
class Bank(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'bank'


class Cart(models.Model):
    cid = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)
    menu_name = models.CharField(max_length=255, blank=True, null=True)
    many = models.IntegerField(blank=True, null=True)
    menu_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=255)
    local = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    payments = models.JSONField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    searching = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Delivery(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=255)
    local = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'delivery'


class Menu(models.Model):
    menu = models.CharField(max_length=255)
    sid = models.ForeignKey('Store', models.DO_NOTHING, db_column='sid')

    class Meta:
        managed = False
        db_table = 'menu'
    
    def __str__(self):
        return self.menu


class Orders(models.Model):
    sid = models.ForeignKey('Store', models.DO_NOTHING, db_column='sid', blank=True, null=True)
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    did = models.ForeignKey(Delivery, models.DO_NOTHING, db_column='did', blank=True, null=True)
    payment = models.JSONField(blank=True, null=True)
    ordert = models.DateTimeField(blank=True, null=True)
    delivert = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    menu_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Seller(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'seller'


class Store(models.Model):
    address = models.CharField(max_length=255)
    sname = models.CharField(max_length=255)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    phone_nums = models.JSONField()
    schedules = models.JSONField()
    seller = models.ForeignKey(Seller, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'store'