from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'translist', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('api/userlist', UserCreateListApiView.as_view()),
    path('api/', include(router.urls)),

]
