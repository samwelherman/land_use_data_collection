from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from django import forms
from .models import *



# class NeighbourInline(admin.TabularInline):
#     model = Neighbour
#     # model = LandCordinate

@admin.register(Owner)
class OwnerAdmin(LeafletGeoAdmin):
    #pass
    list_display = ['fname','lname','gender','marital_status','age','phone']
    list_filter =  ['gender','marital_status']
    search_fields = ['fname','lname','mname','phone']
    

    fieldsets = [
            ('pacel id ',{'fields': [('pacel')]}),
            ('Owner names',{'fields': [('fname', 'mname','lname')]}),
            ('Contacts and identity',{'fields': [('phone','identityNo')]}),
            ('Gender and age',{'fields': [('gender','age','ocuppation')]}),
            ('Others',{'fields': [('marital_status','parcentage_of_share','ownership_type')]}),
            

            ]
    
    # class CustomModelChoiceField1(forms.ModelChoiceField):
    #      def label_from_instance(self, obj):
    #          return  (obj.type)
    # class CustomModelChoiceField2(forms.ModelChoiceField):
    #      def label_from_instance(self, obj):
    #          return  (obj.ownership_type)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'landUse':
    #         return self.CustomModelChoiceField1(queryset=LandUse.objects)
        
    #     elif db_field.name == 'ownership':
    #         return self.CustomModelChoiceField2(queryset=OwnershipType.objects)

    #     return super(OwnerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    # readonly_fields = ['get_parent_name']  # Don't forget this!
    # fieldsets = [('Parent info', {'fields': ['get_parent_name']} )]
    
    # @admin.display(description='Parent')
    # def get_parent_name(self, obj):
    #     return obj.parent.name



@admin.register(Neighbour)
class NeighbourAdmin(admin.ModelAdmin):
    # pass
    list_display = ['neighbour_east','neighbour_west','neighbour_north','neighbour_south']
   
@admin.register(OwnershipType)
class OwnershipAdmin(admin.ModelAdmin):
    # pass
    list_display = ['ownership_type','created_at']


@admin.register(Existing_use)
class LandUseAdmin(admin.ModelAdmin):
    pass
    # list_display = ['type','description']




@admin.register(Ward)
class WardsAdmin(LeafletGeoAdmin):
    pass
    # list_display =('ward_name','ward_code')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass
    list_display =('id','name')
    ordering = ['id']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass
    list_display =('id','name')
    ordering = ['id']
    class CustomModelChoiceField(forms.ModelChoiceField):
         def label_from_instance(self, obj):
             return  (obj.name)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'region':
            return self.CustomModelChoiceField(queryset=Region.objects)

        return super(OwnerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    pass
    # list_display =('id','name')
    ordering = ['id']


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    pass
    # list_display =('id','name')
    ordering = ['id']

@admin.register(Hamlet)
class HAmletAdmin(admin.ModelAdmin):
    pass
    # list_display =('id','name')
    ordering = ['id']

# @admin.register(Pacel)
class PacelAdmin(LeafletGeoAdmin):
    pass
    list_display =('geom','hamlet')
    ordering = ['id']

admin.site.register(Pacel,PacelAdmin)


@admin.register(Institution_type)
class IstitutionTypeAdmin(admin.ModelAdmin):
    pass
    list_display =('name','description')
    # ordering = ['id']


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    pass
    list_display =('name','gender','position','institution')
    # ordering = ['id']

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass
    list_display =('district','name','institution_type','id')
    # ordering = ['id']

@admin.register(Districts)
class DistrictsAdmin(LeafletGeoAdmin):
    pass
    list_display =('district_n','district_c')
    # ordering = ['id']

@admin.register(Topology)
class TopologyAdmin(LeafletGeoAdmin):
    pass
    list_display =('id','name')
    # ordering = ['id']

@admin.register(Proposed_use)
class ProposedUseAdmin(LeafletGeoAdmin):
    pass
    list_display =('id','name')
    # ordering = ['id']


   
