from profiles_api import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profiles', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

