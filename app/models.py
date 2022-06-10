from django.db import models

# Create your models here.

class Todo(models.Model):
    status =(
        ('N', 'New'),
        ('P', 'In Progress'),
        ('C', 'Completed'),
    )
    item = models.CharField(max_length=500)
    status = models.CharField(max_length=1, choices=status, default='N')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
