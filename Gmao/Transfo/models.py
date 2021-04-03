from django.db import models
from DirectCompany.models import DirectCompany 
from AffiliateCompany.models import AffiliateCompany
from Person.models import Person  
from Poste.models import Poste 
# Create your models here.

PRELEVEMENT  = (
    ('nos soins selon le norme CEI 60475','Nos soins'),
    ('vos soins','Vos soins')
)
def get_raison_dessais_default_value() :
    return  {"entretien_annuel":False,"autre_à_preciser":""}
def get_etat_transfo_default_value() :
    return  {"sous_tension":False,"hors_tension_depuis":""}
def get_cuve_déformée_default_value() :
    return {"non":False,"oui_à_preciser":""}
def get_alarme_default_value() :
    return  {"non":False,"oui_à_preciser":""}
def get_declenchement_default_value() :
    return  {"non":False,"oui_à_preciser":""}
def get_presence_de_corps_en_suspension_default_value() :
    return {"non":False,"oui_à_preciser":""}

class SampleCharacteristics(models.Model):
    prevelement_effectue_par = models.CharField(max_length=255,choices=PRELEVEMENT)
    temperature_de_fluide =  models.DecimalField(max_digits=5,decimal_places=2)
    point_de_prelevement = models.CharField(max_length=255)
    date_de_prevelement = models.DateField(auto_now=False,auto_now_add=False)
    date_de_reception = models.DateField(auto_now=False,auto_now_add=False)

class SampleCircumstances(models.Model): 
    raison_dessais = models.JSONField(default=get_raison_dessais_default_value)
    etat_transfo = models.JSONField(default=get_etat_transfo_default_value)
    cuve_déformée = models.JSONField(default=get_cuve_déformée_default_value)
    alarme = models.JSONField(default=get_alarme_default_value)
    declenchement = models.JSONField(default=get_declenchement_default_value)

class VisualObservations(models.Model):
    aspect = models.CharField(max_length=255)
    presence_de_corps_en_suspension = models.JSONField(default=get_presence_de_corps_en_suspension_default_value)

class SampleTestCharacteristics(models.Model): 
    type_dessai = models.CharField(max_length=255)
    appereil_dessaie = models.CharField(max_length=255)
    frequence_dessai = models.CharField(max_length=255)
    nombre_de_mesure = models.IntegerField()
    Norme_dessai = models.CharField(max_length=255)
    type_delectrodes = models.CharField(max_length=255)
    distance_entre_electrodes = models.DecimalField(max_digits=4,decimal_places=2)

class Transfo(models.Model):
    poste = models.ForeignKey(Poste,on_delete=models.CASCADE,blank=True,null=True)
    date_de_fabriquation = models.IntegerField(default=0)
    marque = models.CharField(max_length=255)
    puissance = models.IntegerField(default=0)
    tension_primaire = models.IntegerField(default=0)
    num_serie = models.CharField(max_length=255)
    #annee_de_fabrication_primaire = models.IntegerField(default=0)
    mode_de_refroidissement_dhuile = models.CharField(max_length=255)
    masse_dhuile = models.CharField(max_length=255)
    commutateur_a_vide = models.BooleanField(default=False)
    regleur_en_charge= models.BooleanField(default=False)
    hermetique = models.BooleanField(default=False)
    respirant = models.BooleanField(default=False)
    nombre_de_man_doeuvre = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self):
        return self.marque

class SampleBDVTest(models.Model): 
    avg_value = models.DecimalField(max_digits=7,decimal_places=3)

class BDVValue(models.Model):
    sample_bdv_test = models.ForeignKey(SampleBDVTest,on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=7,decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True,auto_now=False)

"""
class TransfoAnalysis(models.Model):
    transfo = models.ForeignKey(Transfo,on_delete=models.CASCADE,blank=True,null=True)
    name   = models.CharField(max_length=255)
    num_bc = models.CharField(max_length=255)
    person = models.ForeignKey(Person,on_delete=models.SET_NULL,blank=True,null=True)
    affiliate = models.BooleanField(default=False)
    affiliate_company = models.ForeignKey(AffiliateCompany,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)

class Value(models.Model):
    transfo_analysis = models.ForeignKey(TransfoAnalysis,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    value = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    def __str__(self):
        return 'created_at : {date} value : {value} unit : {unit}'.format(created_at=self.created_at,value=self.value,unit=self.unit)

"""
CONCLUSION = (
        ('huile conforme', 'Huile conforme'),
        ('huile à traiter', 'Huile à traiter'),
        ('huile à changer', 'Huile à changer'),
    )
class Sample(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    num_bc = models.CharField(max_length=255)
    person =  models.ForeignKey(Person,on_delete=models.SET_NULL,blank=True,null=True)
    affiliate_company = models.ForeignKey(AffiliateCompany,on_delete=models.CASCADE,blank=True,null=True)
    transfo = models.ForeignKey(Transfo,on_delete=models.CASCADE)
    sample_characteristics = models.OneToOneField(SampleCharacteristics,on_delete=models.CASCADE,blank=True,null=True)
    sample_circumstances = models.OneToOneField(SampleCircumstances,on_delete=models.CASCADE,blank=True,null=True)
    visual_observations = models.OneToOneField(VisualObservations,on_delete=models.CASCADE,blank=True,null=True)
    bdv_test = models.OneToOneField(SampleBDVTest,on_delete=models.CASCADE,blank=True,null=True)
    sample_test_characteristics = models.OneToOneField(SampleTestCharacteristics,on_delete=models.CASCADE,blank=True,null=True)
    conclusion = models.CharField(max_length=255,choices=CONCLUSION,blank=True,null=True)
    recomendation = models.TextField()