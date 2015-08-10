__author__ = 'vitor'

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from django.db import IntegrityError
from core.models import Zipcode
import json


class RestViewPostTest(TestCase):

    def test_post(self):
        #post deve retornar status code 201
        data = {'zip_code': '14800380'}
        resp = self.client.post(r('zipcode_add_n_list'), data)
        self.assertEqual(201, resp.status_code)
        self.assertTrue(Zipcode.objects.exists())

    def test_zipcode_unique(self):
        data = {'zip_code': '14800380'}
        resp = self.client.post(r('zipcode_add_n_list'), data)
        obj = Zipcode(zipcode=u'14800380', address=u'Rua Dona Maria Janasi Biagioni', neighborhood=u'Centro',
                      state=u'SP', city=u'Araraquara')
        self.assertRaises(IntegrityError, obj.save)

    def test_wrong_zipcode(self):
        data = {'zip_code': '1402260'}
        resp = self.client.post(r('zipcode_add_n_list'), data)
        self.assertEqual(404, resp.status_code)


class RestViewListTest(TestCase):

    def setUp(self):
        obj = Zipcode(zipcode=u'14800380', address=u'Rua Dona Maria Janasi Biagioni', neighborhood=u'Centro',
                      state=u'SP', city=u'Araraquara')
        obj.save()
        obj = Zipcode(zipcode=u'14800360', address=u'Rua Padre Duarte', neighborhood=u'Centro',
                      state=u'SP', city=u'Araraquara')
        obj.save()

    def test_list(self):

        resp = self.client.get(r('zipcode_add_n_list'))
        content = json.loads(resp.content)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(2, len(content))

    def test_list_limit(self):

        resp = self.client.get(r('zipcode_add_n_list')+'?limit=1')
        content = json.loads(resp.content)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(content))


class RestViewDetailTest(TestCase):

    def test_get(self):
        obj = Zipcode(zipcode=u'14800380', address=u'Rua Dona Maria Janasi Biagioni', neighborhood=u'Centro',
                      state=u'SP', city=u'Araraquara')
        obj.save()
        resp = self.client.get(r('zipcode_detail_n_delete', args=[obj.zipcode]))
        content = json.loads(resp.content)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(u'14800380', content['zipcode'])
        self.assertEqual(u'Rua Dona Maria Janasi Biagioni', content['address'])
        self.assertEqual(u'Centro', content['neighborhood'])
        self.assertEqual(u'SP', content['state'])
        self.assertEqual(u'Araraquara', content['city'])

    def test_get_404(self):
        obj = Zipcode(zipcode=u'14800380', address=u'Rua Dona Maria Janasi Biagioni', neighborhood=u'Centro',
                      state=u'SP', city=u'Araraquara')
        obj.save()
        resp = self.client.get(r('zipcode_detail_n_delete', args=[14800381]))
        self.assertEqual(404, resp.status_code)


class RestViewDeleteTest(TestCase):

    def test_delete(self):
        obj = Zipcode(zipcode=u'14800380', address=u'Rua Dona Maria Janasi Biagioni', neighborhood=u'Centro',
                      state=u'SP', city=u'Araraquara')
        obj.save()
        resp = self.client.delete(r('zipcode_detail_n_delete', args=[obj.zipcode]))
        self.assertEqual(204, resp.status_code)
        self.assertFalse(Zipcode.objects.exists())

    def test_delete_404(self):
        obj = Zipcode(zipcode=u'14800380', address=u'Rua Dona Maria Janasi Biagioni', neighborhood=u'Centro',
                      state=u'SP', city=u'Araraquara')
        obj.save()
        resp = self.client.delete(r('zipcode_detail_n_delete', args=[14800381]))
        self.assertEqual(404, resp.status_code)
