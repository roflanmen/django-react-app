# allow only loggen in users
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

# advertisement viewset
from .serializers import AdvertisementSerializer
from .models import Advertisement


class AdvertisementViewSet(ModelViewSet):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    @action(methods=["post"], url_path="create", detail=False, permission_classes=[IsAuthenticated])
    def create_advertisement(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        advertisement = serializer.save()

        return Response(
            {
                "title": advertisement.title,
                "description": advertisement.description,
                "owner": advertisement.owner.username,
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request):
        queryset = Advertisement.objects.all()
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        advertisement = self.get_object()

        if request.user.id != advertisement.owner.id:
            raise PermissionDenied("You do not have permission to edit this advertisement.")

        return super().update(request, *args, **kwargs, partial=True)
