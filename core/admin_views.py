from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


# API view to list all users (admin only)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_users(request):
    users = list(User.objects.values(
        'id', 'username', 'email', 'is_staff', 'is_superuser'
    ))
    return Response(users)


# API view to delete a user by ID (admin only)
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    if user:
        user.delete()
        return Response({'success': True})
    return Response({'error': 'User not found'}, status=404)
