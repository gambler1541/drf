from django.contrib.auth import get_user_model

from utils.paginations import SnippetPage
from ..models import Snippet

from snippets.serializers import SnippetBaseSerializer, SnippetDetailSerializer, UserListSerializer, SnippetListSerializer, UserBaseSerializer
from rest_framework import generics
from rest_framework import permissions

User=get_user_model()

__all__ = (
    'SnippetList',
    'SnippetDetail',
    'UserList',
    'UserDetail'
)

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = SnippetPage

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SnippetListSerializer
        elif self.request.method == 'POST':
            return SnippetDetailSerializer


    def perform_create(self, serializer):
        # SnippetBaseSerializer로 전달받은 데이터와
        # 'owner' 항목에 self.request.user데이터를 추가한 후
        # save() 호출, DB에 저장 및 인스턴스 반환
         serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetBaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          # IsOwnerOrReadOnly,
                    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer


