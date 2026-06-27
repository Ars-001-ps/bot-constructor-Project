from django.db import models

class Bot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Scenario(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Step(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    order = models.IntegerField()
    action = models.TextField()

