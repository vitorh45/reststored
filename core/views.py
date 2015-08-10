from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from core.models import Zipcode
import requests
import json


@csrf_exempt
def zipcode_add_n_list(request):
    if request.method == 'POST':
        zipcode = request.POST['zip_code']
        url = settings.POSTMON_URL % zipcode
        try:
            req = requests.get(url).json()
            address = req.get('logradouro', None)
            neighborhood = req.get('bairro', None)
            city = req.get('cidade', None)
            state = req.get('estado', None)
            obj = Zipcode(zipcode=zipcode, address=address, neighborhood=neighborhood, city=city, state=state)
            obj.save()
            return HttpResponse(status=201)
        except Exception, e:
            return HttpResponse(status=404)

    zipcodes = Zipcode.objects.all()
    limit = request.GET.get('limit', None)
    if limit:
        zipcodes = zipcodes[:limit]
    zipcodes_data = [{'zipcode': z.zipcode, 'address': z.address, 'neighborhood': z.neighborhood, 'city': z.city,
                          'state': z.state} for z in zipcodes]
    return HttpResponse(json.dumps(zipcodes_data))


@csrf_exempt
def zipcode_detail_n_delete(request, zipcode):
    if request.method == 'DELETE':
        zipcode = get_object_or_404(Zipcode, zipcode=zipcode)
        zipcode.delete()
        return HttpResponse(status=204)
    zipcode = get_object_or_404(Zipcode, zipcode=zipcode)
    zipcode_data = {'zipcode': zipcode.zipcode, 'address': zipcode.address, 'neighborhood': zipcode.neighborhood,
                    'city': zipcode.city, 'state': zipcode.state}
    return HttpResponse(json.dumps(zipcode_data))