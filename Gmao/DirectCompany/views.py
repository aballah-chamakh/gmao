from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status,generics
from .models import DirectCompany
from .serializers import DirectCompanySerializer
from Transfo.serializers import TransfoSerializer
from Transfo.models import Transfo,Sample,SampleCharacteristics,SampleCircumstances,VisualObservations,SampleTestCharacteristics,SampleTestCharacteristics,SampleBDVTest,BDVValue
from AffiliateCompany.models import AffiliateCompany
from Person.serializers import PersonSerializer
from Poste.serializers import PosteSerializer
from Poste.models import Poste 
from Person.models import Person 
from django.db.models import Q



class DirectCompanyViewSet(viewsets.ModelViewSet):
    serializer_class = DirectCompanySerializer
    queryset = DirectCompany.objects.all()

    @action(methods=['GET'],detail=False)
    def get_person_by_id(self,request):
        person_id = request.GET.get('person_id')
        print(person_id)
        person_obj = Person.objects.get(id=person_id)
        ser = PersonSerializer(person_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

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
        direct_company_obj = self.get_object()
        person_id = request.data.get('person_id')
        print("person_id : "+str(person_id))
        person_obj = Person.objects.get(id=person_id)
        direct_company_obj.persons.remove(person_obj)
        person_obj.delete()
        return Response({'res':'done'},status=status.HTTP_200_OK)
    
    @action(methods=['GET'],detail=False)
    def get_transfo_by_id(self,request):
        transfo_id = request.GET.get('transfo_id')
        transfo_obj = Transfo.objects.get(id=transfo_id)
        ser = TransfoSerializer(transfo_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True)
    def add_transfo(self,request,pk=None):
        direct_company_obj = self.get_object()
        poste_id = request.data.get('poste_id')
        del request.data['poste_id']
        bool_fields = ['commutateur_a_vide','regleur_en_charge','hermetique','respirant']
        print(request.data)
        for bool_field in bool_fields : 
            request.data[bool_field] = True if request.data[bool_field] == "Non" else False
        poste_obj  = Poste.objects.get(id=poste_id)
        transfo_obj = Transfo.objects.create(poste=poste_obj,**request.data)
        ser = TransfoSerializer(transfo_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True)
    def edit_transfo(self,request,pk=None):
        direct_company_obj = self.get_object()
        transfo_id = request.data.get('transfo_id')
        bool_fields = ['commutateur_a_vide','regleur_en_charge','hermetique','respirant']      
        for bool_field in bool_fields : 
            request.data[bool_field] = True if request.data[bool_field] == "Non" else False
        del request.data['transfo_id']
        Transfo.objects.filter(id=transfo_id).update(
                **request.data)
        transfo_obj = Transfo.objects.get(id=transfo_id)
        ser = TransfoSerializer(transfo_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['DELETE'],detail=False)
    def delete_transfo(self,request):
        transfo_id = request.data.get('transfo_id')
        print(type(transfo_id))
        print("transfo_id : "+str(transfo_id))
        transfo_obj = Transfo.objects.get(id=transfo_id)
        transfo_obj.delete()
        return Response({'res':'done'},status=status.HTTP_200_OK)
   
    @action(methods=['GET'],detail=False)
    def get_transfo_analysis_by_id(self,request):
        transfoanalysis_id = request.GET.get('transfo_analysis_id')
        transfoanalysis_obj = TransfoAnalysis.objects.get(id=transfoanalysis_id)
        ser = TransfoAnalysisDetailSerializer(transfoanalysis_obj,many=False)
        print(ser.data['person_name_id'])
        print(ser.data['affiliate_company_name_id'])
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True)
    def add_transfo_analysis(self,request,pk=None):
        transfo_id = request.data.get('transfo_id')
        affiliate_company_name_id = request.data.get("affiliate_company")
        affiliate_company_id = 0
        if(affiliate_company_name_id != None and  len(affiliate_company_name_id.split('_')) > 1) : 
            affiliate_company_id = int(affiliate_company_name_id.split('_')[-1])
        person_name_id = request.data.get('person')
        person_id = 0
        
        if(person_name_id != None and len(person_name_id.split('_')) > 1) : 
            person_id = person_name_id.split('_')[-1]

        transfo_analysis_name = request.data.get('name')
        transfo_analysis_num_bc = request.data.get('num_bc')
        transfo_obj = Transfo.objects.get(id=transfo_id)
        affiliatecompany_obj = None 
        person_obj = None
        if person_id != 0 : 
            person_obj = Person.objects.get(id=person_id)
        if affiliate_company_id != 0 : 
            affiliatecompany_obj = AffiliateCompany.objects.get(id=affiliate_company_id)
        person_obj = Person.objects.get(id=person_id)
        transfo_analysis_obj = TransfoAnalysis.objects.create(
                transfo = transfo_obj,
                name=transfo_analysis_name,
                person=person_obj,
                num_bc=transfo_analysis_num_bc,
                affiliate=True if affiliate_company_id != 0 else False,
                affiliate_company=affiliatecompany_obj,
                )
        ser = TransfoAnalysisSerializer(transfo_analysis_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True)
    def edit_transfo_analysis(self,request,pk=None):
        transfo_id = request.data.get('transfo_id')
        transfo_analysis_id = request.data.get('transfo_analysis_id')
        person_name_id = request.data.get('person')
        affiliate_company_name_id = request.data.get('affiliate_company')
        transfo_analysis_name = request.data.get('name')
        transfo_analysis_num_bc = request.data.get('num_bc')
        transfo_analysis_obj = TransfoAnalysis.objects.get(id=transfo_analysis_id)
        person_obj = None
        print("person_name_id : "+str(person_name_id))
        print("affiliate_company_name_id : "+str(affiliate_company_name_id))
        if person_name_id and len(person_name_id.split('_')) > 1 : 
            person_id = person_name_id.split('_')[-1]
            person_obj = Person.objects.get(id=person_id)
        
        affiliate_company_obj = None
        if  affiliate_company_name_id and len(affiliate_company_name_id.split('_')) >  1 : 
            print("handle it")
            affiliate_company_id = affiliate_company_name_id.split('_')[-1]
            print(type(affiliate_company_id))
            affiliate_company_obj = AffiliateCompany.objects.get(id=int(affiliate_company_id))
            print(affiliate_company_obj)
        print("person_obj : "+str(person_obj))
        print("affiliate_company_obj : "+str(affiliate_company_obj))
        transfo_obj = Transfo.objects.get(id=transfo_id)
        TransfoAnalysis.objects.filter(id=transfo_analysis_id).update(
                transfo = transfo_obj,
                name=transfo_analysis_name,
                person=person_obj,
                num_bc=transfo_analysis_num_bc,
                affiliate= True if affiliate_company_obj else False ,
                affiliate_company=affiliate_company_obj,
        )
        transfo_analysis_obj = TransfoAnalysis.objects.get(id=transfo_analysis_id)
        ser = TransfoAnalysisDetailSerializer(transfo_analysis_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)

    @action(methods=['DELETE'],detail=False)
    def delete_transfo_analysis(self,request):
        transfo_analysis_id = request.data.get('transfo_analysis_id')
        print("transfo_analysis_id :: ")
        print(transfo_analysis_id)
        transfo_analysis_obj = TransfoAnalysis.objects.get(id=transfo_analysis_id)
        transfo_analysis_obj.delete()
        return Response({'res':'done'},status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False)
    def get_transfo_analysis_value_by_id(self,request):
        transfo_analysis_value_id = request.GET.get('transfo_analysis_value_id')
        transfo_analysis_value_obj = Value.objects.get(id=transfo_analysis_value_id)
        ser = ValueSerializer(transfo_analysis_value_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)
    @action(methods=['POST'],detail=True)
    def edit_transfo_analysis_value(self,request,pk=None):
        transfo_analysis_value_id = request.data.get('transfo_analysis_value_id')
        del request.data['transfo_analysis_value_id']
        Value.objects.filter(id=transfo_analysis_value_id).update(
            **request.data 
        )
        transfo_analysis_value_obj = Value.objects.get(id=transfo_analysis_value_id)
        ser = ValueSerializer(transfo_analysis_value_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)
    @action(methods=['POST'],detail=True)
    def add_transfo_analysis_value(self,request,pk=None):
        transfo_analysis_id = request.data.get('transfo_analysis_id')
        del request.data['transfo_analysis_id']
        transfo_analysis_obj = TransfoAnalysis.objects.get(id=transfo_analysis_id)
        transfo_analysis_value_obj = Value.objects.create(transfo_analysis=transfo_analysis_obj,**request.data)
        ser = ValueSerializer(transfo_analysis_value_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)
    @action(methods=['DELETE'],detail=False)
    def delete_transfo_analysis_value(self,request):
        transfo_analysis_value_id = request.data.get('transfo_analysis_value_id')
        transfo_analysis_value_obj = Value.objects.get(id=transfo_analysis_value_id)
        transfo_analysis_value_obj.delete()
        return Response({'msg':'done'},status=status.HTTP_200_OK)
    @action(methods=['POST'],detail=True)
    def add_poste(self,request,pk=None):
        direct_company_obj = self.get_object()
        request.data['lat'] = float(request.data['lat']) if request.data['lat'] != "" else 0
        request.data['lng'] = float(request.data['lng']) if request.data['lng'] != "" else 0 
        print(request.data)
        poste_obj = Poste.objects.create(direct_company=direct_company_obj,**request.data)
        return Response({'res':'done'},status=status.HTTP_200_OK)
    @action(methods=['POST'],detail=True)
    def edit_poste(self,request,pk=None):
        poste_id = request.data.get('poste_id')
        del request.data['poste_id']
        Poste.objects.filter(id=poste_id).update(**request.data)
        updated_poste_obj = Poste.objects.get(id=poste_id)
        ser = PosteSerializer(updated_poste_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)
    @action(methods=['GET'],detail=True)
    def get_poste_by_id(self,request,pk=None):
        poste_id = request.GET.get('poste_id')
        poste_obj = Poste.objects.get(id=poste_id)
        ser = PosteSerializer(poste_obj,many=False)
        return Response(ser.data,status=status.HTTP_200_OK)
    @action(methods=['DELETE'],detail=False)
    def delete_poste_by_id(self,request):
        poste_id = request.data.get('poste_id')
        poste_obj = Poste.objects.get(id=post_id)
        poste_obj.delete()
        return Response({'res':'done'},status=status.HTTP_200_OK)
    @action(methods=['POST'],detail=True)
    def add_sample(self,request,pk=None):
        transfo_id = request.data.get('transfo_id')
        transfo_obj = Transfo.objects.get(id=transfo_id)
        num_bc = request.data['num_bc']
        person_name_id = request.data['person_name']
        affiliate_company_name_id = request.data['affiliate_company_name']
        person_obj = None 
        affiliate_company_obj = None 
        print(person_name_id)
        if person_name_id :
            person_name_id = person_name_id.split("__")[:-1]
            print("here :: ")
            print(person_name_id)
            person_id  = person_name_id[-1]
            person_obj = Person.objects.get(id=person_id)
        if affiliate_company_name_id : 
            affiliate_company_id = affiliate_company_name_id.split("__")[-1]
            affiliate_company_obj = AffiliateCompany(id=affiliate_company_id)
        sample_obj = Sample.objects.create(transfo=transfo_obj,
                                            num_bc = num_bc,
                                            affiliate_company = affiliate_company_obj,
                                            person = person_obj)
        return Response({'res':'done'},status=status.HTTP_200_OK)
    @action(methods=['DELETE'],detail=False)
    def delete_sample_by_id(self,request):
        sample_id = request.data.get('sample_id')
        sample_obj = Sample.objects.get(id=sample_id)
        sample_obj.delete()
        return Response({'res':'done'},status=status.HTTP_200_OK)