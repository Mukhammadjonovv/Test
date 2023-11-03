from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'suv', SuvViewSet)
router.register(r'mijoz', MijozViewSet)
router.register(r'buyurtma', BuyurtmaViewSet)
router.register(r'admin', AdminViewSet)
router.register(r'haydovchi', HaydovchiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
