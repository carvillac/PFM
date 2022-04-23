# Carlos Villacastín Ruiz
# PFM - Máster Avanzado de Programación en Python para Hacking, BigData y Machine Learning I
# Fichero PatientService.py 
# Clase que modela el objeto Paciente.
# 23/04/2022

import json

class patient(object):

    def __init__(self,data):
            try:
                self.name = data['name']
                self.surname =  data['surname']
                self.age = data['age']
                self.clumpThickness = data['clumpThickness']
                self.uniformityCellSize = data['uniformityCellSize']
                self.uniformityCellShape = data['uniformityCellShape']
                self.marginalAdhesion = data['marginalAdhesion']
                self.singleEpiCellSize = data['singleEpiCellSize']
                self.bareNuclei = data['bareNuclei']
                self.blandChromatin = data['blandChromatin']
                self.normalNucleoli = data['normalNucleoli']
                self.mitoses = data['mitoses']
            except:
                print("There was an error creatring the object")

    def to_json(self):
       return json.dumps(self.__dict__)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname
    
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_clumpThickness(self):
        return self.clumpThickness

    def set_clumpThickness(self, clumpThickness):
        self.clumpThickness = clumpThickness

    def get_uniformityCellSize(self):
        return self.uniformityCellSize

    def set_uniformityCellSize(self, uniformityCellSize):
        self.uniformityCellSize = uniformityCellSize

    def get_uniformityCellShape(self):
        return self.uniformityCellShape

    def set_uniformityCellShape(self, uniformityCellShape):
        self.uniformityCellSize = uniformityCellShape

    def get_marginalAdhesion(self):
        return self.marginalAdhesion

    def set_marginalAdhesion(self, marginalAdhesion):
        self.marginalAdhesion = marginalAdhesion

    def get_singleEpiCellSize(self):
        return self.singleEpiCellSize

    def set_singleEpiCellSize(self, singleEpiCellSize):
        self.singleEpiCellSize = singleEpiCellSize

    def get_bareNuclei(self):
        return self.bareNuclei

    def set_bareNuclei(self, bareNuclei):
        self.bareNuclei = bareNuclei

    def get_blandChromatin(self):
        return self.blandChromatin

    def set_blandChromatin(self, blandChromatin):
        self.blandChromatin = blandChromatin
    
    def get_normalNucleoli(self):
        return self.normalNucleoli

    def set_normalNucleoli(self, normalNucleoli):
        self.normalNucleoli = normalNucleoli

    def get_mitoses(self):
        return self.mitoses

    def set_mitoses(self, mitoses):
        self.mitoses = mitoses

    def get_tumorData(self):
         dataList = [self.get_clumpThickness(),
          self.get_uniformityCellSize(),
          self.get_uniformityCellShape(),
          self.get_marginalAdhesion(),
          self.get_singleEpiCellSize(),
          self.get_bareNuclei(),
          self.get_blandChromatin(),
          self.get_normalNucleoli(),
          self.get_mitoses()]
         return dataList
   