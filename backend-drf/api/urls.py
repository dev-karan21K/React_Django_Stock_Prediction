from django.urls import path
from accounts import views as UserViews
from .views import StockPreditionAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserViews.RegisterView.as_view()),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('protected-view/', UserViews.ProtectedView.as_view()),
    
    #prediction api
    path('predict/', StockPreditionAPIView.as_view(), name='stock_prediction'),
]
