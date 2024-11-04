from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet, RatingViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
]
