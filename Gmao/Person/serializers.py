from rest_framework import serializers
from .models import Person 


class PersonSerializer(serializers.ModelSerializer):
    company_detail = serializers.SerializerMethodField()
    class Meta : 
        model = Person 
        fields = ('id','functionality','phone_number','email','first_name','last_name','created_at','company_detail',)
    def get_company_detail(self,person_obj):
        affiliate_company_qs = person_obj.affiliatecompany_set.all()
        print("get_company_detail : ")
        print(affiliate_company_qs.count())
        if affiliate_company_qs.count() > 0:
            affiliate_company_obj = affiliate_company_qs.first()
            affiliate_company_name = affiliate_company_obj.name
            print({'type':'affiliate_company','name':affiliate_company_name,'affiliate_company_id':affiliate_company_obj.id})
            return {'type':'affiliate_company','name':affiliate_company_name,'affiliate_company_id':affiliate_company_obj.id}
        else : 
            direct_company_qs = person_obj.directcompany_set.all()
            if direct_company_qs.count() > 0 : 
                direct_company_name = direct_company_qs.first().name 
                return {'type':'direct_company','name':direct_company_name}
        return None