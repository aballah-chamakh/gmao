from rest_framework import serializers 
from .models import DirectCompany
from Person.serializers import PersonSerializer 
from Poste.serializers import PosteSerializer



class DirectCompanySerializer(serializers.ModelSerializer):
    persons = serializers.SerializerMethodField()
    postes = serializers.SerializerMethodField()
    class Meta : 
        model = DirectCompany 
        fields = ('id','persons','address','city','email','tel','country','postes','name','created_at')
    def get_persons(self,direct_company_obj):
        qs = direct_company_obj.persons.all()
        ser = PersonSerializer(qs,many=True)
        print("person list  : ")
        print(ser.data)
        return ser.data 
    def get_postes(self,direct_company_obj):
        qs = direct_company_obj.poste_set.all()
        ser = PosteSerializer(qs,many=True)
        print("poste list  : ")
        print(qs)
        print(ser.data)
        return ser.data 