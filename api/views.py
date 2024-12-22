from rest_framework import viewsets
from .models import Category, Product, Review, Order
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, OrderSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer,userSerializer,WishlistSerializer
from .models import Wishlist
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrReadOnly,IsStaffOrReadOnly,IsSuperUser,IsStaffUser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated] 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly] 

    # Add filtering and searching
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'price']  # Filter by category or price
    search_fields = ['name', 'description']  # Search by product name or description
    #custom filtering
    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]



#user list
class UserListView(APIView):
    """
    API to list all registered users. Accessible only by superusers.
    """
    permission_classes = [IsStaffUser, IsSuperUser]

    def get(self, request):
        users = User.objects.all()  # Fetch all registered users
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class SuperUserOnlyView(APIView):
    """
    API endpoint accessible only by superusers.
    """
    permission_classes = [IsAuthenticated, IsSuperUser]

    def get(self, request):
        data = {
            "message": "Welcome, Superuser!",
            "superuser_data": {
                "username": request.user.username,
                "email": request.user.email,
            }
        }
        return Response(data)

#is_straff_view

class StrafUserOnlyView(APIView):
    """
    API endpoint accessible only by superusers.
    """
    permission_classes = [IsAuthenticated ,IsStaffUser]

    def get(self, request):
        data = {
            "message": "Welcome, Superuser!",
            "user": {
                "username": request.user.username,
                "email": request.user.email,
            }
        }
        return Response(data)


#staff user list view

class StaffUserListView(APIView):
    """
    API to list all staff users.
    """
    permission_classes = [IsSuperUser]

    def get(self, request):
        # Filter only staff users
        staff_users = User.objects.filter(is_staff=True)
        serializer = UserSerializer(staff_users, many=True)
        return Response(serializer.data)


#super user list view
    
class SuperUserListView(APIView):
    """
    API to list all superUser users.
    """
    permission_classes = [IsSuperUser]

    def get(self, request):
        # Filter only super users
        super_users = User.objects.filter(is_superuser=True)
        serializer = userSerializer(super_users, many=True)
        return Response(serializer.data)




# User Management Views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'username': token.user.username})

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."})

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not user.check_password(serializer.validated_data['old_password']):
            return Response({"error": "Old password is incorrect."}, status=400)

        try:
            validate_password(serializer.validated_data['new_password'], user=user)
        except ValidationError as e:
            return Response({"error": e.messages}, status=400)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"message": "Password updated successfully."})
    

#wishlist view
    
class WishlistListCreateView(generics.ListCreateAPIView):
    """
    List all wishlist items of the logged-in user and allow adding new items.
    """
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishlistDeleteView(generics.DestroyAPIView):
    """
    Delete an item from the wishlist.
    """
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)