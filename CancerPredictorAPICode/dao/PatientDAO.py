# Carlos Villacastín Ruiz
# PFM - Máster Avanzado de Programación en Python para Hacking, BigData y Machine Learning I
# Fichero PatientDAO.py 
# Clase que ejecuta las querys contra la BD.
# 23/04/2022

import pymongo
from sqlite3 import Error
from model.Patient import patient
from bson.objectid import ObjectId
import json

class patient_dao:

    def insert(db, patient):
        try:
            dbResponse = db.patients.insert_one(patient.__dict__)
            return dbResponse.inserted_id
        except Exception as ex:
            print(ex)
            raise ex

    def update(db, id, patient):
        try:
            dbResponse = db.patients.update_one(
                {"_id": ObjectId(id)},
                {"$set": patient.__dict__})
            return dbResponse.modified_count
        except Exception as ex:
            print(ex)
            raise ex

    def delete(db, id):
        try:
            dbResponse = db.patients.delete_one({"_id": ObjectId(id)})
            return dbResponse.deleted_count
        except Exception as ex:
            print(ex)

    def list(db, skip, limit):
        try:
            data = list(db.patients.find().skip(skip).limit(limit))
            return data
        except Exception as ex:
            print(ex)
            raise ex

    def getPatient(db, id):
        try:
            data = list(db.patients.find({"_id": ObjectId(id)}))
            return data
        except Exception as ex:
            print(ex)
            raise ex

            
