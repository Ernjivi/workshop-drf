from django.db import models

class Client(models.Model):
    """
    Client model.
    """

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Domain(models.Model):
    """
    Client Model
    """

    client = models.ForeignKey(Client, on_delete=models.CASCADE,
        related_name='domains')
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    foo = models.PositiveSmallIntegerField(null=True)
