from rest_framework import serializers 
from .models import AffiliateCompany
from Person.serializers import PersonSerializer 
class AffiliateCompanySerializer(serializers.ModelSerializer):
    persons = serializers.SerializerMethodField()
    class Meta : 
        model = AffiliateCompany
        fields = ('id','name','address','city','country','email','tel','persons','created_at')
    def get_persons(self,affiliate_company_obj):
        qs = affiliate_company_obj.persons.all()
        ser = PersonSerializer(qs,many=True)
        return ser.data 
