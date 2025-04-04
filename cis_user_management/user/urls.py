from django.urls import path
from .views import (
    UserListCreateAPIView, UserDetailAPIView, ReactivateUserAPIView,
    DeactivateUserAPIView, ChangePasswordAPIView, SignupAPIView,
    LoginAPIView, LogoutAPIView
)

urlpatterns = [
    path('user_list/', UserListCreateAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('<int:pk>/reactivate/', ReactivateUserAPIView.as_view(), name='user-reactivate'),
    path('<int:pk>/deactivate/', DeactivateUserAPIView.as_view(), name='user-deactivate'),
    path('<int:pk>/change-password/', ChangePasswordAPIView.as_view(), name='user-change-password'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
