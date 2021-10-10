from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Food(models.Model):
    foodName = models.CharField(max_length=100)
    containsProteins = models.BooleanField(default=False)
    containsFish = models.BooleanField(default=False)
    containsVegetables = models.BooleanField(default=False)
    isMainCourse = models.BooleanField(default = True)
    lastEaten = models.DateTimeField(blank=True, null=True)
    #foodImage = models.ImageField(upload_to='recipes',null=True, blank=True, default=None)
    foodImageURL = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.foodName

# class Meal(models.Model):
#     mealName = models.CharField(max_length=100, blank=True, null=True)
#     mealComposition = models.ManyToManyField(Food)
#     def __str__(self):
#         return self.mealName

class Kid(models.Model):
    kidName = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.kidName

class Score(models.Model):
    kid = models.ForeignKey(Kid, related_name='kid_details',on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='scores', on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)])
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.kid.kidName + ' ' + self.food.foodName



class DateMenu(models.Model):
    date = models.DateField()
    mealTime = models.CharField(choices = [('Lunch', 'Lunch'),('Dinner', 'Dinner')], max_length=10)
    food = models.ForeignKey(Food, related_name='dates', blank=True, null=True, on_delete=models.SET_NULL)
    customization = models.CharField(max_length=100)
    def __str__(self):
        return str(self.date) + ' ' + str(self.mealTime)

