from rest_framework import fields, serializers

from .models import Council, District, Existing_use, Hamlet, Institution, Institution_type, Owner, OwnershipType, Pacel, Proposed_use, Region,Representative, Topology, Village, Ward


# serializers for sending data to the Flutter APP
class InstitutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution_type
        fields = (
             'id','name','description'
        )

class OwnershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnershipType
        fields = (
             'id','ownership_type'
        )

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
             'id','zone_id','name'
        )

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
             'id','name','region'
        )


class CouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Council
        fields = (
             'id','name','district'
        )

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = (
             'id','name','council'
        )

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = (
             'id','name','ward'
        )

# class HamletSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hamlet
#         fields = (
#              'id','name','village'
#         )

class TopologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Topology
        fields = (
             'id','name'
        )

class ExistingUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Existing_use
        fields = (
              'id','name'
        )

class ProposedUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposed_use
        fields = (
              'id','name'
        )
#serializer to get Data from the flutter App 
class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = '__all__'
        depth =1 

class nstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
        depth =1 

class PacelSerializer(serializers.ModelSerializer):
    institution = nstitutionSerializer()
    class Meta:
        model = Representative
        fields = '__all__'
        depth =1 
    
    def create(self, validated_data):
         user_data = validated_data.pop('institution')
         print(user_data)
         original_user_data = self.initial_data.get('institution')
         user_serializer = nstitutionSerializer(data=validated_data)
         user_serializer.is_valid(raise_exception=True)
         user_serializer.save()
        #  validated_data['sam'] = user
         return super(PacelSerializer, self).create(validated_data)
     