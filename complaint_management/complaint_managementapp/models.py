from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)

    class Meta:
        db_table = "contact"
class Customer(models.Model):
    email = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "customer"
class Administration(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "administration"
class AddCatagory(models.Model):
    title = models.CharField(max_length=100)
    descreption = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "addcatagory"
class Solvers(models.Model):
    email = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    class Meta:
        db_table = "Solvers"
class Update_Status(models.Model):
    addcatagory = models.ForeignKey(AddCatagory, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    class Meta:
        db_table = "Update_Status"

class Send_Query(models.Model):
    title = models.CharField(max_length=100)
    descreption = models.CharField(max_length=100)
    solvers = models.CharField(max_length=100)

    class Meta:
        db_table = "Send_Query"
class Replay(models.Model):
    solvers = models.ForeignKey(Solvers, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)

    class Meta:
        db_table = "Replay"
