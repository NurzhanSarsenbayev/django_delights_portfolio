from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit} @ ${self.unit_price}/{self.unit}"
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.menu_item} - {self.ingredient} - {self.quantity}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date = models.DateTimeField()

    PENDING = "PN"
    IN_PROGRESS = 'IP'
    FINISHED = 'FD'
    CANCELLED = 'CF'

    PURCHASE_STATUS = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
        (CANCELLED, 'Cancelled')
    ]

    status = models.CharField(max_length=2, choices=PURCHASE_STATUS, default=PENDING)

    def __str__(self):
        return f"Purchase of {self.menu_item.title} on {self.date} - Status: {self.get_status_display()}"
