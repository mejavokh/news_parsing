from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=220)
    link = models.CharField(max_length=220)

    def __str__(self):
        return self.title


class Articles(models.Model):
    title = models.CharField(max_length=220)
    description = models.CharField(max_length=220)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
