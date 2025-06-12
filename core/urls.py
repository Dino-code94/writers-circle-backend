from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, VoteView
from .auth_views import RegisterView, LoginView
from .admin_views import list_users, delete_user
from .profile_views import user_profile


# DRF router for posts & comments
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    # Django admin site route
    path('admin/', admin.site.urls),

    # API routes under /api/
    path('api/', include([
        path('', include(router.urls)),  # CRUD routes for posts and comments
        path('vote/<int:post_id>/', VoteView.as_view(), name='vote'),
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),

        # Admin-only API routes
        path(
            'admin/users/',
            list_users,
            name='list-users'
        ),
        path(
            'admin/delete_user/<int:user_id>/',
            delete_user,
            name='delete-user'
        ),


        # User profile API route
        path('user/', user_profile, name='user-profile'),
    ])),
]
