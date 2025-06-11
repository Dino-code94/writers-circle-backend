from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, VoteView
from .auth_views import RegisterView, LoginView

# DRF router for posts & comments
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes under /api/
    path('api/', include([
        path('', include(router.urls)),
        path('vote/<int:post_id>/', VoteView.as_view(), name='vote'),
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),
    ])),
]
