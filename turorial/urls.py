from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from api.views import RegisterView, LoginView, LogoutView, ProfileView, ChangePasswordView,CategoryViewSet,ProductViewSet,ReviewViewSet,OrderViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/signup/', RegisterView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/profile/', ProfileView.as_view(), name='profile'),
    path('api/auth/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('api/auth/password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/auth/password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('api/auth/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/auth/password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api/', include(router.urls)),
]
