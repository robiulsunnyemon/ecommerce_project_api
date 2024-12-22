from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from api.views import RegisterView, LoginView, LogoutView, ProfileView, ChangePasswordView,CategoryViewSet,ProductViewSet,ReviewViewSet,OrderViewSet,UserListView,SuperUserOnlyView,StrafUserOnlyView,StaffUserListView,SuperUserListView,WishlistListCreateView, WishlistDeleteView

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
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/superuser/', SuperUserOnlyView.as_view(), name='superuser-endpoint'),
    path('api/staff-only/', StrafUserOnlyView.as_view(), name='staff-only'),
    path('api/staff-users/', StaffUserListView.as_view(), name='staff-users-list'),
    path('api/super-users/', SuperUserListView.as_view(), name='super-users-list'),

    path('api/wishlist/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('api/wishlist/<int:pk>/', WishlistDeleteView.as_view(), name='wishlist-delete'),

]
