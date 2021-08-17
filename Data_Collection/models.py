from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.db.models.base import Model




# Create your models here.
class ComonFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OwnershipType(ComonFields):
    ownership_type = models.CharField(max_length=200)
    def _unicode_(self):
        return self.ownership_type
        




class Institution_type(ComonFields):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def _unicode_(self):
        return self.name

class Region(models.Model):
    zone_id = models.BigIntegerField()
    name = models.CharField(max_length=200)

    def _unicode_(self):
        return self.name

class District(models.Model):
    region = models.ForeignKey(Region,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def _unicode_(self):
        return self.name

class Council(models.Model):
    district = models.ForeignKey(District,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def _unicode_(self):
        return self.name

class Ward(models.Model):
    council = models.ForeignKey(Council,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def _unicode_(self):
        return self.name

class Village(models.Model):
    ward = models.ForeignKey(Ward,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def _unicode_(self):
        return self.name

class Hamlet(models.Model):
    village = models.ForeignKey(Village,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def _unicode_(self):
        return self.name




class Topology(ComonFields):
    name = models.CharField(max_length=200)
    def _unicode_(self):
        return self.name
class Existing_use(ComonFields):
    name = models.CharField(max_length=200)
    def _unicode_(self):
        return self.name

class Proposed_use(ComonFields):
    name = models.CharField(max_length=200)
    def _unicode_(self):
        return self.name

class Pacel(ComonFields):
    geom = models.MultiPolygonField(srid=4326)
    hamlet = models.ForeignKey(Hamlet,null=True, on_delete=models.CASCADE)
    village = models.ForeignKey(Village,null=True, on_delete=models.CASCADE)
    topology = models.CharField(max_length=200)
    existing_use = models.CharField(max_length=200)
    proposed_use = models.CharField(max_length=200)
    objects = GeoManager()

    def _unicode_(self):
        return self.geom
class Owner(ComonFields):
    pacel = models.ForeignKey(Pacel,null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200)
    mname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    identityNo = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    ocuppation = models.CharField(max_length=200)
    parcentage_of_share = models.IntegerField()
    ownership_type = models.CharField(max_length=200)
    

    def _unicode_(self):
        return self.fname

    class Meta:
        # app_label = string_with_title("stuffapp", "The stuff box")
        # 'stuffapp' is the name of the django app
        verbose_name = 'Land Owner'
        verbose_name_plural = 'Owner Details '

class Guardian(ComonFields):
    name = models.CharField(max_length=200)
    age = models.BigIntegerField()
    gender =  models.CharField(max_length=200)
    marital_status =  models.CharField(max_length=200)
    relationship =  models.CharField(max_length=200)
    owner = models.ForeignKey(Owner,null=True, on_delete=models.CASCADE)
    def _unicode_(self):
        return self.name

class Probate(ComonFields):
    name = models.CharField(max_length=200)
    age = models.BigIntegerField()
    gender =  models.CharField(max_length=200)
    marital_status =  models.CharField(max_length=200)
    relationship =  models.CharField(max_length=200)
    owner = models.ForeignKey(Owner,null=True, on_delete=models.CASCADE)
    def _unicode_(self):
        return self.name




class Source_of_income(ComonFields):
    owner = models.ForeignKey(Owner,null=True, on_delete=models.CASCADE)
    income_type = models.CharField(max_length=200)
    number = models.IntegerField()

    def _unicode_(self):
        return self.income_type





class Institution(ComonFields):
    pacel = models.ForeignKey(Pacel,null=True, on_delete=models.CASCADE)
    institution_type = models.ForeignKey(Institution_type,null=True, on_delete=models.CASCADE)
    district = models.ForeignKey(District,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def _unicode_(self):
        return self.name

class Representative(ComonFields):
    institution = models.ForeignKey(Institution,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    def _unicode_(self):
        return self.name
        
class Person_with_interest(ComonFields):
    name = models.CharField(max_length=200)
    age = models.BigIntegerField()
    gender =  models.CharField(max_length=200)
    marital_status =  models.CharField(max_length=200)
    relationship =  models.CharField(max_length=200)
    pacel = models.ForeignKey(Pacel,null=True, on_delete=models.CASCADE)
    def _unicode_(self):
        return self.name


class Neighbour(ComonFields):
    neighbour_east = models.CharField(max_length=200)
    neighbour_west = models.CharField(max_length=200)
    neighbour_south = models.CharField(max_length=200)
    neighbour_north = models.CharField(max_length=200)
    pacel = models.ForeignKey(Pacel,null=True, on_delete=models.CASCADE)

class Distances(ComonFields):
    from_school = models.IntegerField()
    froh_hospital = models.IntegerField()
    from_water = models.IntegerField()
    from_market = models.IntegerField()
    household_type1 = models.IntegerField(null=True)
    household_type2 = models.IntegerField(null=True)
    household_type3 = models.IntegerField(null=True)
    household_type4 = models.IntegerField(null=True)
    pacel = models.ForeignKey(Pacel,null=True, on_delete=models.CASCADE)

class Disputies(ComonFields):
    description = models.CharField(max_length=2000)
    pacel = models.ForeignKey(Pacel,null=True, on_delete=models.CASCADE)




# class Attachment(models.Model):
#     owner_id= models.BigIntegerField()
#     document_name = models.CharField(max_length=20)
#     path = models.CharField(max_length=20)

#     def _unicode_(self):
#         return self.document_name

class Districts(models.Model):
    district_c = models.CharField(max_length=50)
    district_n = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    
    def _unicode_(self):
        return self.district_n



