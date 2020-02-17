from django.db import models
import datetime


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateField(datetime.datetime.now)
    updated = models.DateField(datetime.datetime.now)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)

class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(datetime.timezone)
    recipes = models.ManyToManyField(Recipe, through="RecipePlan")

class DayName(models.Model):
    name = models.CharField(max_length=16)
    order = models.IntegerField(unique=True)

class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField()
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)



