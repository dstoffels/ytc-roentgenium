from .models import Reply
from rest_framework import serializers

class ReplySerializer(serializers.ModelSerializer):
  class Meta:
    model = Reply
    fields= ['id', 'comment_id', 'text', 'username', 'user_id']
    depth = 1

  username = serializers.SerializerMethodField()

  def get_username(self, reply):
    return reply.user.username