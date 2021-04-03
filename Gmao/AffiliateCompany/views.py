from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status,generics
from .models import AffiliateCompany
from .serializers import AffiliateCompanySerializer
from Person.models import Person 
from Person.serializers import PersonSerializer
from django.db.models import Q



class AffiliateCompanyViewSet(viewsets.ModelViewSet):
    serializer_class = AffiliateCompanySerializer
    queryset = AffiliateCompany.objects.all()


    @action(methods=['POST'],detail=True)
    def add_person(self,request,pk=None):
        direct_company_obj = self.get_object()
        person_obj = Person.objects.create(**request.data)
        direct_company_obj.persons.add(person_obj)
        ser = PersonSerializer(person_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True)
    def edit_person(self,request,pk=None):
        direct_company_obj = self.get_object()
        person_id = request.data.get('person_id')
        del request.data['person_id']
        Person.objects.filter(id=person_id).update(
            **request.data ,
        )
        person_obj = Person.objects.get(id=person_id)
        ser = PersonSerializer(person_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['DELETE'],detail=True)
    def delete_person(self,request,pk=None):
        affiliate_company_obj = self.get_object()
        person_id = request.data.get('person_id')
        person_obj = Person.objects.get(id=person_id)
        affiliate_company_obj.persons.remove(person_obj)
        person_obj.delete()
        return Response({'res':'done'},status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False)
    def get_person_by_id(self,request):
        person_id = request.GET.get('person_id')
        person_obj = Person.objects.get(id=person_id)
        ser = PersonSerializer(person_obj)
        return Response(ser.data,status=status.HTTP_200_OK)




   
