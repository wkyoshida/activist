from rest_framework import viewsets
from .models import Resource, Task, Topic, ResourceTopic, TopicFormat
from .serializers import (
    ResourceSerializer, 
    TaskSerializer, 
    TopicSerializer,
    ResourceTopicSerializer, 
    TopicFormatSerializer
    )


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class ResourceTopicViewSet(viewsets.ModelViewSet):
    queryset = ResourceTopic.objects.all()
    serializer_class = ResourceTopicSerializer

class TopicFormatViewSet(viewsets.ModelViewSet):
    queryset = TopicFormat.objects.all()
    serializer_class = TopicFormatSerializer
