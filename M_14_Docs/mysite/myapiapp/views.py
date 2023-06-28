from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema

from .serializers import GroupSerializer, HelloSerializer


@extend_schema(summary="Simple Hello world view",
               description="Just returns Hello World and no more...",
               responses={
                   200: HelloSerializer,
               })
@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({"message": "Hello World!"})


class GroupsListView(ListCreateAPIView):
    permission_classes = []
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    search_fields = [
        "user",
        "delivery_address",
        "promocode",
        "products",
    ]
