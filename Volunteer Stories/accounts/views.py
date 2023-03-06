from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework import views, viewsets, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken


from .models import UserModel, ImageModel, VolunteerModel
from .serializers import LoginSerializer, UserModelSerializer, LogoutSerializer, ImageModelSerializer, \
    VolunteerSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            user_data = UserModelSerializer.List(user).data
            tokens = get_tokens_for_user(user)
            return Response({'data': user_data, "tokens": tokens, }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LogoutAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data['refresh_token']
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = UserModel.objects.all()
    search_fields = ['username', 'email']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserModelSerializer.List
        return UserModelSerializer.Write

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_admin:
            return UserModel.objects.all()
        return UserModel.objects.filter(id=self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_admin:
            user = UserModel.objects.get(id=kwargs['pk'])
            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data}, status=HTTP_200_OK)
        elif request.user.id == int(kwargs['pk']):
            user = UserModel.objects.get(id=kwargs['pk'])
            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data}, status=HTTP_200_OK)
        return Response({'message': 'You are not authorized to perform this action'}, status=HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        if request.user.is_admin:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data}, status=HTTP_200_OK)
        return Response({'message': 'You are not authorized to perform this action'}, status=HTTP_400_BAD_REQUEST)


class ImageModelViewSet(ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer
    permission_classes = [IsAuthenticated]


class VolunteerModelViewSet(ModelViewSet):
    queryset = VolunteerModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return VolunteerSerializer.Write
        return VolunteerSerializer.List
