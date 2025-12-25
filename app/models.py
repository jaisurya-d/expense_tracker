from django.db import models

# Create your models here.

"""
| Field           | Use             |
| --------------- | --------------- |
| `CharField`     | Short text      |
| `TextField`     | Long text       |
| `IntegerField`  | Numbers         |
| `FloatField`    | Decimal numbers |
| `BooleanField`  | True / False    |
| `EmailField`    | Emails          |
| `DateField`     | Dates           |
| `DateTimeField` | Date + time     |
| `ImageField`    | Images          |
| `FileField`     | Files           |
-------------------------------------

name = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    default="Anonymous"
)


"""

class Expense(models.Model):
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"