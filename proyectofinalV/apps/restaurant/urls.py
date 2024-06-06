from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'restaurants',RestaurantViewSet,basename='restaurants')
router.register(r'tables',TableViewSet,basename='tables')
router.register(r'orders',OrderViewSet,basename='orders')
router.register(r'bills',BillsViewSet,basename='bills')
router.register(r'waiters',WaiterViewSet,basename='waiters')


urlpatterns= [
]

urlpatterns += router.urls