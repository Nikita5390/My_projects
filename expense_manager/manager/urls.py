from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'translist', TransactionViewSet, basename='transaction')
router.register(r'cat', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/userlist', UserCreateListApiView.as_view()),
    path('api/', include(router.urls)),

    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
