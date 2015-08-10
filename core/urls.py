__author__ = 'vitor'

from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'core.views.zipcode_add_n_list', name='zipcode_add_n_list'),
    url(r'^(?P<zipcode>[\w_-]+)/$', 'core.views.zipcode_detail_n_delete', name='zipcode_detail_n_delete'),
]