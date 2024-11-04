from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    released_at = models.DateField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies")
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def avg_rating(self):
        return self.ratings.aggregate(models.Avg('score'))['score__avg'] or 0

    @property
    def total_ratings(self):
        return self.ratings.count()
    
    def __str__(self):
        return self.title
    
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        unique_together = ('movie', 'user')

    def __str__(self):
        return f"{self.movie} - {self.score}"


class Report(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie} reported by {self.reported_by}"



