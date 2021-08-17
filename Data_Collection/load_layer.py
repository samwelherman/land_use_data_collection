import os
# from pathlib import Path
from .models import Districts
from django.contrib.gis.utils import LayerMapping

wards_mapping = {
    'region_cod': 'Region_Cod',
    'region_nam': 'Region_Nam',
    'district_c': 'District_C',
    'district_n': 'District_N',
    'ward_code': 'Ward_Code',
    'ward_name': 'Ward_Name',
    'pop2002': '2002Pop',
    'pop2012': '2012Pop',
    'wardspopch': 'WardsPopCh',
    'geom': 'MULTIPOLYGON',
}

districts_mapping = {
    'district_c': 'District_C',
    'district_n': 'District_N',
    'geom': 'MULTIPOLYGON',
}


districts_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Districts.shp'))
# wards_shp = Path(__file__).resolve().parent / 'data' / 'tanzania_wards.shp'

def run(verbose=True):
    # pass
    lm = LayerMapping(Districts, districts_shp, districts_mapping, transform= False,encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)