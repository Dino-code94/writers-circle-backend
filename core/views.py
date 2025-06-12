from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# ViewSet to handle full CRUD for Post model
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Automatically assign post author to logged-in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ViewSet to handle full CRUD for Comment model
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Automatically assign comment author to logged-in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# APIView for voting system (upvote & downvote logic)
class VoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        # Try to retrieve post
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)

        # Handle vote actions
        action = request.data.get('action')
        if action == 'upvote':
            post.votes += 1
        elif action == 'downvote':
            post.votes -= 1
        else:
            return Response({'error': 'Invalid action'}, status=400)

        post.save()
        return Response({'votes': post.votes})
