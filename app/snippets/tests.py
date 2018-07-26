import json
import random

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from snippets.models import Snippet
from snippets.serializers import SnippetBaseSerializer, UserListSerializer

User = get_user_model()
DUMMY_USER_USERNAME = 'dummy_username'
def get_dummy_user():
    return User.objects.create_user(username=DUMMY_USER_USERNAME)


class SnippetListTest(APITestCase):
    """
    Snippet List요청에 대한 테스트
    :return:
    """
    URL ='/snippets/generic_cbv/snippets/'
    def test_status_code(self):
        """
        요청 결과의 HTTP상태코드가 200인지 확인
        :return:
        """
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_snippet_list_count(self):
        """
        Snippet List를 요청시 DB에 잇는 자료수와 같은 갯수가 리턴되는지 테스트
        :return:
        """
        user=get_dummy_user()
        for i in range(1, 10):
            Snippet.objects.create(code=f'a = {i}', owner = user)
        response = self.client.get(self.URL)
        data = json.loads(response.content)
        self.assertEqual(data['count'], Snippet.objects.count())




    def test_snippet_list_order_by_created_descending(self):
        """
        Snippets List의 결과가 생성일자 내림차순인지 확인
        :return:
        """
        user = get_dummy_user()
        for i in range(random.randint(5, 10)):
            Snippet.objects.create(code=f'a = {i}', owner=user)

        pk_list=[]
        page=1
        while True:
            response = self.client.get(self.URL, {'page': page})
            data = json.loads(response.content)
            pk_list += [item['pk'] for item in data['results']]
            if data['next']:
                page += 1
            else:
                break
        self.assertEqual(
            # JSON으로 전달받은 데이터에서 pk만 꺼낸 리스트
            pk_list,
            # DB에서 created역순으로 pk만 가져온 QuerySet으로 만든 리스트
            list(Snippet.objects.order_by('created').values_list('pk', flat=True))
        )


CREATE_DATA = '''{
    "code": "print('hello, world')"
}'''
class SnippetsCreateTest(APITestCase):
    URL = '/snippets/generic_cbv/snippets/'

    def test_snippet_create_status_code(self):
        '''
        201이 들어오는지
        :return:
        '''

        # 실제 JSON형식 데이터를 전송
        # response = self.client.post('/snippets/django_view/snippets/',data = CREATE_DATA, content_type='application/json',)
        user = get_dummy_user()

        self.client.force_authenticate(user=user)
        response = self.client.post(
            self.URL,
            data = {
                'code':"print('hello, world')",
            },
            format='json',)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_snippet_create_save_db(self):
        '''
        요청 후 실제 DB에 저장되엇는지
        '''
        snippet_data = {
            'title': 'SnippetTitle',
            'code' : 'SnippetCode',
            'linenos': True,
            'language': 'c',
            'style': 'monokai',
        }

        user = get_dummy_user()

        self.client.force_authenticate(user=user)
        response = self.client.post(
            self.URL,
            data=snippet_data,
            format='json',
        )


        data = json.loads(response.content)
        check_fields = ['title', 'linenos', 'language', 'style']
        for field in check_fields:
            self.assertEqual(data[field], snippet_data[field])

        self.assertEqual(data['owner'], UserListSerializer(user).data)


    def test_snippet_create_missing_code_raise_exception(self):
        '''
        'code'데이터가 주어지지 않을 경우 적절한 Exception이 발생하는지
        :return:
        '''
        snippet_data = {
            'title': 'SnippetTitle',
            'linenos': True,
            'language': 'c',
            'style': 'monokai',
        }

        user = get_dummy_user()
        self.client.force_authenticate(user=user)

        response = self.client.post(
            self.URL,
            data=snippet_data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
