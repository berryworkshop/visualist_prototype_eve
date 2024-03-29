from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins, generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from .serializers import (
    UserSerializer, GroupSerializer, RecordSerializer
)
from .models import Record, Relation


def base_view(req):
    return JsonResponse({'foo': 'bar'})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows records to be viewed or edited.
    """
    queryset = Record.objects.filter(is_primary=True)
    serializer_class = RecordSerializer


class EventViewSet(RecordViewSet):
    """
    API endpoint for all records which are events.
    """
    queryset = RecordViewSet.queryset.filter(label='event')


class EntityViewSet(RecordViewSet):
    """
    API endpoint for all records which are entities.
    """
    queryset = RecordViewSet.queryset.filter(
        Q(label='person') | Q(label='organization'))
