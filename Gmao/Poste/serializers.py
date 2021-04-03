from rest_framework import serializers 
from .models import Poste
from Transfo.serializers import TransfoSerializer

class PosteSerializer(serializers.ModelSerializer):
    transfos = serializers.SerializerMethodField()
    direct_company_name  = serializers.SerializerMethodField()
    class Meta : 
        model = Poste 
        fields = ('id','created_at','direct_company_name','transfos','name','regie','lat','lng',)
    def get_transfos(self,poste_obj):
        transfo_qs = poste_obj.transfo_set.all()
        print(transfo_qs)
        ser = TransfoSerializer(transfo_qs,many=True)
        return ser.data
    def get_direct_company_name(self,poste_obj):
        if poste_obj.direct_company : 
            return poste_obj.direct_company.name 
        return None 