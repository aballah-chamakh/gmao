from rest_framework import serializers 
from Person.serializers import PersonSerializer
from Person.models import Person 
from AffiliateCompany.models import AffiliateCompany
from Transfo.models import Transfo
from AffiliateCompany.serializers import AffiliateCompanySerializer
from .models import Transfo,SampleBDVTest,BDVValue,SampleCharacteristics,SampleCircumstances,VisualObservations,SampleTestCharacteristics,Sample 



"""
class ValueSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Value
        fields = ('id','value','unit','created_at')

class TransfoAnalysisSerializer(serializers.ModelSerializer):
    values = serializers.SerializerMethodField()
    person_name = serializers.SerializerMethodField()
    affiliate_company_name = serializers.SerializerMethodField()
    class Meta : 
        model = TransfoAnalysis
        fields = ('id','name','num_bc','created_at','values','person_name','affiliate_company_name')
    def get_values(self,transfo_analysis_obj):
        qs = transfo_analysis_obj.value_set.all()
        ser = ValueSerializer(qs,many=True)
        return ser.data 
    def get_affiliate_company_name(self,transfo_analysis_obj):
        if transfo_analysis_obj.affiliate_company : 
            return transfo_analysis_obj.affiliate_company.name 
        return ""
    def get_person_name(self,transfo_analysis_obj):
        if transfo_analysis_obj.person : 
            return transfo_analysis_obj.person.name 
        return ""

class TransfoAnalysisDetailSerializer(serializers.ModelSerializer):
    values = serializers.SerializerMethodField()
    person_name = serializers.CharField(source="person.name")
    affiliate_company_name = serializers.SerializerMethodField()
    affiliate_companies = serializers.SerializerMethodField()
    persons = serializers.SerializerMethodField()
    person_name_id = serializers.SerializerMethodField()
    affiliate_company_name_id = serializers.SerializerMethodField()
    class Meta : 
        model = TransfoAnalysis
        fields = ('id','name','num_bc','created_at','values','person_name','affiliate_company_name','persons','affiliate_companies','person_name_id','affiliate_company_name_id')
    def get_values(self,transfo_analysis_obj):
        qs = transfo_analysis_obj.value_set.all()
        ser = ValueSerializer(qs,many=True)
        return ser.data 
    def get_affiliate_company_name(self,transfo_analysis_obj):
        if transfo_analysis_obj.affiliate_company : 
            return transfo_analysis_obj.affiliate_company.name 
        return ""
    def get_affiliate_companies(self,transfo_obj):
        qs = AffiliateCompany.objects.all()
        ser =  AffiliateCompanySerializer(qs,many=True)
        return ser.data
    def get_persons(self,transfo_obj):
        qs = Person.objects.all()
        ser = PersonSerializer(qs,many=True)
        return ser.data
    def get_affiliate_company_name_id(self,transfo_analysis_obj):
        affiliate_company_obj = transfo_analysis_obj.affiliate_company
        if affiliate_company_obj : 
            return affiliate_company_obj.name.replace(' ','_')+"_"+str(affiliate_company_obj.id)
        return ""
    def get_person_name_id(self,transfo_analysis_obj):
        person_obj = transfo_analysis_obj.person 
        if person_obj : 
            return person_obj.name.replace(' ','_')+"_"+str(person_obj.id) 
        return ""
"""

class VisualObservationsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = VisualObservations
        fields =('id','aspect','presence_de_corps_en_suspension')


class SampleCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = SampleCharacteristics
        fields = ('prevelement_effectue_par_nos_soins','norme_de_prelevement','temperature_de_fluide','date_de_reception',)

class SampleCircumstancesSerializer(serializers.ModelSerializer):
    class Meta : 
        model = SampleCircumstances
        fields = ('raison_dessais','etat_transfo','cuve_déformée','alarme','declenchement',)   

class SampleCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = VisualObservations
        fields = ('aspect','presence_de_corps_en_suspension',)

class SampleTestCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = SampleTestCharacteristics
        fields = ('type_dessai','appereil_dessaie','frequence_dessai','nombre_de_mesure','Norme_dessai','type_delectrodes','distance_entre_electrodes',) 

class BDVValueSerializer(serializers.ModelSerializer):
    class Meta : 
        model = SampleTestCharacteristics
        fields = ('value','created_at','updated_at',) 

class SampleBDVTestSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source="image.url")
    bdv_values = serializers.SerializerMethodField() 
    class Meta : 
        model = SampleTestCharacteristics
        fields = ('avg_value','image','bdv_values')
    def get_bdv_values(self,sample_bdv_test_obj):
        bdv_value_qs = sample_bdv_test_obj.bdvvalue_set.all()
        ser = BDVValueSerializer(bdv_value_qs,many=True)
        return ser.data 

class SampleSerializer(serializers.ModelSerializer):
    sample_characteristics = serializers.SerializerMethodField()
    sample_circumstances = serializers.SerializerMethodField()
    visual_observations = serializers.SerializerMethodField()
    sample_test_characteristics = serializers.SerializerMethodField()
    bdv_test = serializers.SerializerMethodField() 
    person_name = serializers.SerializerMethodField()
    affiliate_company_name = serializers.SerializerMethodField()
    class Meta : 
        model = Sample 
        fields = ('created_at','num_bc','bdv_test','person_name','affiliate_company_name','sample_characteristics','sample_circumstances','visual_observations','sample_test_characteristics','conclusion','recomendation')
    def get_person_name(self,sample_obj):
        if sample_obj.person : 
            person_obj = sample_obj.person
            return person_obj.first_name+" "+person_obj.last_name  
        return ""
    def get_affiliate_company_name(self,sample_obj):
        if sample_obj.affiliate_company : 
            affiliate_company_obj = sample_obj.affiliate_company
            return affiliate_company_obj.name 
        return ""
    def get_sample_characteristics(self,sample_obj):
        sample_characteristics_obj = sample_obj.sample_characteristics
        if sample_characteristics_obj :
            ser = SampleCharacteristicsSerializer(sample_characteristics_obj,many=False)
            return ser.data 
        return None 
    def get_sample_circumstances(self,sample_obj):
        sample_circumstances_obj = sample_obj.sample_circumstances 
        if sample_circumstances_obj : 
            ser = SampleCircumstancesSerializer(sample_circumstances_obj,many=False)
            return ser.data
        return None  
    def get_visual_observations(self,sample_obj):
        visual_observations_obj = sample_obj.visual_observations
        if visual_observations_obj : 
            ser = VisualObservationsSerializer(visual_observations_obj,many=False)
            return ser.data 
        return None 
    def get_sample_test_characteristics(self,sample_obj):
        sample_test_characteristics_obj = sample_obj.sample_test_characteristics
        if sample_test_characteristics_obj : 
            ser = SampleTestCharacteristicsSerializer(sample_test_characteristics_obj)
            return None 
        return None 
    def get_bdv_test(self,sample_obj):
        bdv_test_obj = sample_obj.bdv_test
        if bdv_test_obj :
            ser = SampleBDVTestSerializer(bdv_test_obj,many=False)
            return ser.data 
        return None 

class TransfoSerializer(serializers.ModelSerializer):
    affiliate_companies = serializers.SerializerMethodField()
    persons = serializers.SerializerMethodField()
    direct_company_name = serializers.SerializerMethodField()
    direct_company_id = serializers.SerializerMethodField()
    poste_name = serializers.SerializerMethodField()
    poste_id = serializers.SerializerMethodField()
    samples = serializers.SerializerMethodField()
    class Meta : 
        model = Transfo 
        fields = ('id','samples','num_serie','nombre_de_man_doeuvre','respirant','hermetique','regleur_en_charge','commutateur_a_vide','masse_dhuile','mode_de_refroidissement_dhuile','marque','puissance','tension_primaire','direct_company_name','direct_company_id','created_at','affiliate_companies','persons','poste_id','poste_name',)    
   
    def get_affiliate_companies(self,transfo_obj):
        qs = AffiliateCompany.objects.all()
        ser =  AffiliateCompanySerializer(qs,many=True)
        return ser.data
    def get_persons(self,transfo_obj):
        qs = Person.objects.all()
        ser = PersonSerializer(qs,many=True)
        return ser.data
    def get_poste_name(self,transfo_obj):
        print(transfo_obj)
        if transfo_obj.poste : 
            return transfo_obj.poste.name 
        return None 
    def get_poste_id(self,transfo_obj):
        if transfo_obj.poste : 
            return transfo_obj.poste.id 
        return None 
    def get_direct_company_name(self,transfo_obj):
        print("here baby !!!!!")
        print(type(transfo_obj))
        print(transfo_obj)
        if transfo_obj.poste : 
            return transfo_obj.poste.direct_company.id 
        return None 
    def get_direct_company_id(self,transfo_obj):
        if transfo_obj.poste  : 
            return transfo_obj.poste.direct_company.name 
        return None 
    def get_samples(self,transfo_obj):
        qs = transfo_obj.sample_set.all() 
        ser = SampleSerializer(qs,many=True)
        return ser.data 