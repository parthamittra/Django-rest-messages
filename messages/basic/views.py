from models import Message
from rest_framework import viewsets
from messages.basic.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('created_date')
    serializer_class=MessageSerializer
