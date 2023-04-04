from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('advocate', views.AdvocateViewSet, basename='advocate')
router.register('company', views.CompanyViewSet, basename='company')
# router.register(r'advocate/(?P<username>\w+)/', views.AdvocateViewSet, basename='advocate_detail')


urlpatterns = [
    path('', include(router.urls)),
]