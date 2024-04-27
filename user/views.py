from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import PermissionDenied
from .models import Profile
from rest_framework import status

from .serializers import RegistrationSerializer, UserRetrieveSerializer


class UserViewSet(ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = Profile.objects.all()

    @action(
        methods=["post"], url_path="create", detail=False, permission_classes=[AllowAny]
    )
    def registration(self, request: Request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request):
        queryset = Profile.objects.all()
        serializer = UserRetrieveSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user = self.get_object()

        if request.user.id != user.id:
            raise PermissionDenied("You do not have permission to edit this user.")

        return super().update(request, *args, **kwargs, partial=True)
