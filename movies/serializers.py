from rest_framework import serializers
from .models import Movie, Rating, Report

class MovieSerializer(serializers.ModelSerializer):
    avg_rating = serializers.ReadOnlyField()
    total_ratings = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'released_at', 'duration', 'genre', 'language', 'created_by', 'created_at', 'updated_at', 'avg_rating', 'total_ratings']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'movie', 'user', 'score']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'movie', 'reported_by', 'details']

