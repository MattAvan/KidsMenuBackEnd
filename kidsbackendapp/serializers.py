from rest_framework import serializers
from .models import Kid, Food, Score, DateMenu
#from django.shortcuts import get_object_or_404
from drf_extra_fields.fields import Base64ImageField

class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = ['id','kidName','color']

class ScoreSerializer(serializers.ModelSerializer):
    kid = KidSerializer(many=False)

    class Meta:
        model=Score
        fields = ['id','food','kid','score','comment']
        read_only_fields = ('food',)

    def to_internal_value(self, data):
        self.fields['kid'] = serializers.PrimaryKeyRelatedField(
            queryset=Kid.objects.all())
        return super(ScoreSerializer, self).to_internal_value(data)

class DateMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model=DateMenu
        fields= ['id','date','mealTime','food']

class FoodSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)
    foodImage = Base64ImageField(required=False)
    dates = serializers.SlugRelatedField(many=True, read_only=True, slug_field='date')
    class Meta:
        model = Food
        fields = ['id',
                  'foodName',
                  'containsProteins',
                  'containsFish',
                  'containsVegetables',
                  'isMainCourse',
                  'lastEaten',
                  'scores',
                  'foodImage',
                  'dates']

    def create(self, validated_data):
        scores_data = validated_data.pop('scores')
        food = Food.objects.create(**validated_data)
        for score_data in scores_data:
            Score.objects.create(food=food, **score_data)
        return food

    def update(self, instance, validated_data):
        scores = list((instance.scores).all())

        instance.foodName = validated_data.get('foodName', instance.foodName)
        instance.containsProteins = validated_data.get('containsProteins', instance.containsProteins)
        instance.containsFish = validated_data.get('containsFish', instance.containsFish)
        instance.containsVegetables = validated_data.get('containsVegetables', instance.containsVegetables)
        instance.isMainCourse = validated_data.get('isMainCourse', instance.isMainCourse)
        instance.lastEaten = validated_data.get('lastEaten', instance.lastEaten)
        instance.foodImage = validated_data.get('foodImage', instance.foodImage)
        instance.save()

        for score_data in scores_data:
            score = scores.pop(0)
            score.kid = score_data.get('kid', score.kid)
            score.score = score_data.get('score', score.score)
            score.comment = score_data.get('comment', score.comment)
            score.save()

        return instance





