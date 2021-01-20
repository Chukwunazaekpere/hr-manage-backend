from django.db import models


class Store(models.Model):
    data = models.Field()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.data