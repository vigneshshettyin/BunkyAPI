from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView


class BaseViewSet(ListCreateAPIView, viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)