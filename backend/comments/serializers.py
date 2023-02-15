from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'text', 'likes', 'dislikes', 'user_id', 'username']
    depth = 0

  user_id = serializers.IntegerField(write_only=True)
  # username = serializers.SerializerMethodField()

  # def get_username(self, comment):
  #   return comment.user.username