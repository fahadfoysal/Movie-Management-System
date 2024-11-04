from rest_framework import viewsets, permissions
from .models import Movie, Rating, Report
from .serializers import MovieSerializer, RatingSerializer, ReportSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import IsCreatorOrReadOnly
from rest_framework.permissions import AllowAny

class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsCreatorOrReadOnly, IsAdminUser]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]
