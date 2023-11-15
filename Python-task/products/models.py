from django.db import models


class Product(models.Model):
    maker = models.CharField(max_length=10)
    model = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.type} {self.maker} {self.model}"


class PC(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    speed = models.IntegerField()
    ram = models.IntegerField()
    hd = models.IntegerField()
    cd = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.model.type} {self.model.maker} {self.model.model}"


class Laptop(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    speed = models.IntegerField()
    ram = models.IntegerField()
    hd = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    screen = models.IntegerField()

    def __str__(self):
        return f"{self.model.type} {self.model.maker} {self.model.model}"


class Printer(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=1)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.model.type} {self.model.maker} {self.model.model}"


class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    computer = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promo_computer')
    printer = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promo_printer')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
