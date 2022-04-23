# Carlos Villacastín Ruiz
# PFM - Máster Avanzado de Programación en Python para Hacking, BigData y Machine Learning I
# Fichero PatientService.py 
# Clase dque hace las funciones de Servicio. Conecta el controlador con el DAO y hace la lógica de negocio.
# 23/04/2022

from sqlite3 import Error
from model.Patient import patient
from dao.PatientDAO import patient_dao
import pickle

class patient_service:

    def getCancerPrediction(db, id):
        try:
            data = patient_dao.getPatient(db,id)
            print(data)
            patientResult =patient(data[0])
            tumorData = patientResult.get_tumorData()
            filename = "./resources/CancerPredictor.pkl"
            
            loaded_model = pickle.load(open(filename, "rb"))

            return loaded_model.predict([tumorData])
        except Exception as ex:
            print(ex)
            raise ex

    def insert(db, patient):
        try:
            return patient_dao.insert(db,patient)
        except Exception as ex:
            print(ex)
            raise ex

    def update(db, id, patient):
        try:
            return patient_dao.update(db,id,patient)
        except Exception as ex:
            print(ex)
            raise ex

    def delete(db, id):
        try:
            return patient_dao.delete(db,id)
        except Exception as ex:
            print(ex)
            raise ex

    def list(db, skip, limit):
        try:
            return patient_dao.list(db,skip, limit)
        except Exception as ex:
            print(ex)
            raise ex
