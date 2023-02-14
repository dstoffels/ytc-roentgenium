from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.
@api_view(['GET'])
def comments_table(req, video_id):
  comments = Comment.objects.filter(video_id=video_id)
  ser = CommentSerializer(comments, many=True)
  return Response (ser.data, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def add_comment(req, video_id):
  if req.method == 'POST':
    ser = CommentSerializer(data=req.data)
    ser.is_valid(raise_exception=True)
    ser.save(user=req.user, video_id=video_id)
    return Response(ser.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_comment(req, video_id, comment_id):
  if req.method == 'PUT':
    comment = get_object_or_404(Comment, id=comment_id)
    ser = CommentSerializer(comment, data=req.data)
    ser.is_valid(raise_exception=True)
    ser.save()
    return Response(ser.data, status=status.HTTP_200_OK)

