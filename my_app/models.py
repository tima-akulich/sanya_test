from django.db import models


class SomeModel(models.Model):
    field1 = models.CharField(max_length=10)
    field2 = models.IntegerField()

    def __str__(self):
        return self.field1
