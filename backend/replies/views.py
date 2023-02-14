from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Reply
from .serializers import ReplySerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def replies_table(req, video_id, comment_id):
  if req.method == 'GET':
    replies = Reply.objects.filter(comment_id=comment_id)
    ser = ReplySerializer(replies, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)
  elif req.method == 'POST':
    reply = ReplySerializer(data=req.data)
    reply.is_valid(raise_exception=True)
    reply.save(user=req.user, comment_id=comment_id)
    return Response(reply.data, status=status.HTTP_201_CREATED)