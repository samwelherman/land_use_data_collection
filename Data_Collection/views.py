from django.http import JsonResponse, response
from django.shortcuts import render
from django.http import HttpResponse
from .filters import DistrictFilter

#third part import
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .serializers import *
from .models import *

# Create your views here.

def dashboard(request):
    return render(request,'dashboard/index.html')
def tableView(request):
    
    return render(request,'pages/tableview.html')
def mapView(request):
    return render(request,'pages/mapview.html')
def chartView(request):
    return render(request,'pages/chartview.html')
def analyticView(request):
    return render(request,'pages/analyticview.html')



def filter(request,id):
    if id == 1:
        return render(request,'pages/tablefilter.html')
    elif id == 2:
        return render(request,'pages/mapfilter.html')
    else:
        return render(request,'pages/analyticfilter.html')


    


class GetConfig(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Institution_type.objects.all(), 'serializer_class': InstitutionTypeSerializer},
        {'queryset': OwnershipType.objects.all(), 'serializer_class': OwnershipTypeSerializer},
        {'queryset': Region.objects.all(), 'serializer_class': RegionSerializer},
        {'queryset': District.objects.all(), 'serializer_class': DistrictSerializer},

        {'queryset': Council.objects.all(), 'serializer_class': CouncilSerializer},

        {'queryset': Ward.objects.all(), 'serializer_class': WardSerializer},

        {'queryset': Village.objects.all(), 'serializer_class': VillageSerializer},

        # {'queryset': Hamlet.objects.all(), 'serializer_class': HamletSerializer},

        {'queryset': Topology.objects.all(), 'serializer_class': TopologySerializer},

        {'queryset': Existing_use.objects.all(), 'serializer_class': ExistingUseSerializer},

        {'queryset': Proposed_use.objects.all(), 'serializer_class': ProposedUseSerializer}
        
     ]



class SendData(APIView):
    def post(self, request, *args, **kwargs):
    
        print(request.data)
        # instituions = Institution(name=request.data["institution"]["name"])
        # instituions.save()
        # eid = Institution.objects.filter(id=instituions.id)
        # print(instituions.id)
      
        # representative = Representative(name=request.data["name"],gender=request.data["gender"],position=request.data["position"],institution=instituions)
        # representative.save()
      
        
        return Response(request.data)

