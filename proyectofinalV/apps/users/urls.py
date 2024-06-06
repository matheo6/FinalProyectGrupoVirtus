from .models import *
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)
from django.urls import path

router=DefaultRouter()
router.register(r'users',UserViewSet,basename='users')
router.register(r'waiters',WaiterViewSet,basename='waiters')

urlpatterns= [
    
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh')
]

 
urlpatterns += router.urls