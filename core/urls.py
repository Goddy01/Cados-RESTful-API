from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register('advocate', views.AdvocateViewSet, basename='advocate')
router.register('company', views.CompanyViewSet, basename='company')
# router.register(r'advocate/(?P<username>\w+)/', views.AdvocateViewSet, basename='advocate_detail')


urlpatterns = [
    path('', include(router.urls)),
    
    # URL to the view that genertaes the token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]