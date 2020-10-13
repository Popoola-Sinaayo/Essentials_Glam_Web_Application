from django.test import TestCase
from django.test import Client
from .views import *
from Essential_Glams.models import Mail_Subscriber
from .urls import *
# Create your tests here.


class UrltestModelTests(TestCase):
    '''def url_work(self):
        index_1 = views.index
        self.assertIs(index_1, True)
'''

    def test_models(self):
        s = Mail_Subscriber(Email_Subscribers="Sinaayo@gmail.com")
        s.save()
        self.assertIs(s, 'Sinaayo@gmail.com')

    def test_views(self):
        client = Client()
        r = client.get('/login')
        a = r.status_code
        c = r.content
        self.assertIs(a, 200)
