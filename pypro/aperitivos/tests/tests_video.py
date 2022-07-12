import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


#def test_status_code(resp):
 #   assert resp.status_code == 200


#def test_titulo_video(resp):
#    assert_contains(resp, '<h1>Video Aperitivo: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="http://www.youtube.com/embed/M7lc1UVf-VE?autoplay=1&origin"')
