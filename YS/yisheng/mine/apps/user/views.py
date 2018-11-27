from .serializers import *
from rest_framework.views import APIView
import logging
from .helper import testLogin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
logger = logging.getLogger(__name__)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'positions': reverse('position-list', request=request, format=format),
        'roles': reverse('role-list', request=request, format=format),
        'tokens': reverse('token-list', request=request, format=format),
    })
class UserDetail(APIView):
    """
    检索，更新或删除一个user示例。
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            pass

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    """
    列出所有的snippets或者创建一个新的snippet。
    """

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PositionDetail(APIView):
    """
    检索，更新或删除一个user示例。
    """
    def get_object(self, pk):
        try:
            return Position.objects.get(pk=pk)
        except Position.DoesNotExist:
            pass

    def get(self, request, pk, format=None):
        position = self.get_object(pk)
        serializer = PositionSerializer(position)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        position = self.get_object(pk)
        serializer = PositionSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        position = self.get_object(pk)
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoelDetail(APIView):
    """
    检索，更新或删除一个user示例。
    """
    def get_object(self, pk):
        try:
            return Roel.objects.get(pk=pk)
        except Roel.DoesNotExist:
            pass

    def get(self, request, pk, format=None):
        roel = self.get_object(pk)
        serializer = RoelSerializer(roel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        roel = self.get_object(pk)
        serializer = RoelSerializer(Roel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        roel = self.get_object(pk)
        roel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TokenDetail(APIView):
    """
    检索，更新或删除一个user示例。
    """

    def get_object(self, pk):
        try:
            return Token.objects.get(pk=pk)
        except Token.DoesNotExist:
            pass

    def get(self, request, pk, format=None):
        token = self.get_object(pk)
        serializer = TokenSerializer(token)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        token = self.get_object(pk)
        serializer = TokenSerializer(token, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        token = self.get_object(pk)
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class UserAPIView(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# #
# # class OrganizationViewSet(viewsets.ModelViewSet):
# #     queryset = Organization.objects.all()
# #     serializer_class = OrganizationSerializer
# #
# # class DepartmentViewSet(viewsets.ModelViewSet):
# #     queryset = Department.objects.all()
# #     serializer_class = DepartmentSerializer
# #
# class PositionAPIView(APIView):
#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
#
# class RoelAPIView(APIView):
#     queryset = Roel.objects.all()
#     serializer_class = RoelSerializer
#
# class TokenAPIView(APIView):
#     queryset = Token.objects.all()
#     serializer_class = TokenSerializer