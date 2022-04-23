# Carlos Villacastín Ruiz
# PFM - Máster Avanzado de Programación en Python para Hacking, BigData y Machine Learning I
# Fichero server.py 
# Python Principal que hace las funciones de controlador.
# 23/04/2022

from email import message
from flask import Flask, Response, request, jsonify
import pymongo
import json
from flask_expects_json import expects_json
from model.Patient import patient
from service.PatientService import patient_service

app = Flask(__name__)

#Establecemos la conexión con la BD
try:
    mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS = 1000)
    db = mongo.hospital
    mongo.server_info()
except:
    print("ERROR - Cannot conect to the Mongo DB")

# Función encargada de crear los objetos de respuesta del API
# response - Datos que irán en el mensaje
# code - Codigo devuelto
def createResponse(response, code):
    try:
        return Response(
            response=json.dumps(response),
            status=code,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex) 
        return  Response(
             response=json.dumps(
                {"message": "ERROR Internal"}),
            status=500,
            mimetype="application/json"
        )

######################################################################
# Entrada del API para la inserción de un paciente en la Base de Datos
######################################################################
#Esquema para la validación de datos en el insert.
insertSchema = {
  "type": "object",
  "properties": {
    "name": { "type": "string"},
    "surname": { "type": "string" },
    "age": { "type": "number", "minimum": 0,"maximum": 100},
    "clumpThickness": { "type": "number","minimum": 0,"maximum": 10},
    "uniformityCellSize": { "type": "number","minimum": 0,"maximum": 10 },
    "uniformityCellShape": { "type": "number","minimum": 0,"maximum": 10 },
    "marginalAdhesion": { "type": "number","minimum": 0,"maximum": 10 },
    "singleEpiCellSize": { "type": "number","minimum": 0,"maximum": 10 },
    "bareNuclei": { "type": "number","minimum": 0,"maximum": 10 },
    "blandChromatin": { "type": "number","minimum": 0,"maximum": 10 },
    "normalNucleoli": { "type": "number","minimum": 0,"maximum": 10 },
    "mitoses": { "type": "number","minimum": 0,"maximum": 10 }
  },
  "required": ["name", "surname", "age","clumpThickness","uniformityCellSize","uniformityCellShape","marginalAdhesion",
  "singleEpiCellSize", "bareNuclei", "blandChromatin", "normalNucleoli", "mitoses"]
}

#Ruta
@app.route("/insertPatient", methods=["POST"])
#Validación de datos
@expects_json(insertSchema)
def insert_patient():
    try:
        input = request.get_json()
        id = patient_service.insert(db,patient(input))
        return createResponse({"message": "Patient inserted suscessfully",
                "id": f"{id}"}, 200)
    except Exception as ex:
        print(ex)
        return createResponse({"message":"ERROR inserting the patient"}, 500)

#####################################################################
#Entrada del API para la obtención del listado de pacientes de la BD
#####################################################################
#Esquema para la validación de datos en la obtención de datos.
getPatientsSchema = {
  "type": "object",
  "properties": {
    "skip": { "type": "number"},
    "limit": { "type": "number" }
  },
  "required": ["skip", "limit"]
}

#Ruta
@app.route("/getPatients", methods=["GET"])
#Validación de datos
@expects_json(getPatientsSchema)
def get_list_patients():
    try:
        skip = request.get_json()["skip"]
        limit  = request.get_json()["limit"]
        data = patient_service.list(db,skip,limit)
        for pat in data:
            pat["_id"] = str(pat["_id"])
        
        return createResponse( {"message": "Patient list got suscessfully",
                 "list":  f"{data}"}, 200)
    except Exception as ex:
        print(ex)
        return createResponse({"message": "ERROR getting the list of patient"}, 500)

###############################################################
#Entrada del API para la actualización de un paciente en la BD
###############################################################
#Esquema para la validación de datos en el update.
updateSchema = {
  "type": "object",
  "properties": {
    "name": { "type": "string"},
    "surname": { "type": "string" },
    "age": { "type": "number", "minimum": 0,"maximum": 100},
    "clumpThickness": { "type": "number","minimum": 0,"maximum": 10},
    "uniformityCellSize": { "type": "number","minimum": 0,"maximum": 10 },
    "uniformityCellShape": { "type": "number","minimum": 0,"maximum": 10 },
    "marginalAdhesion": { "type": "number","minimum": 0,"maximum": 10 },
    "singleEpiCellSize": { "type": "number","minimum": 0,"maximum": 10 },
    "bareNuclei": { "type": "number","minimum": 0,"maximum": 10 },
    "blandChromatin": { "type": "number","minimum": 0,"maximum": 10 },
    "normalNucleoli": { "type": "number","minimum": 0,"maximum": 10 },
    "mitoses": { "type": "number","minimum": 0,"maximum": 10 }
  }
}

#Ruta
@app.route("/updatePatient/<id>", methods=["PATCH"])
#Validación
@expects_json(updateSchema)
def update_patient(id):
    try:
        input = request.get_json()
        counter = patient_service.update(db,id,patient(input))
        if (counter > 0):
            return createResponse({"message": "Patient updated suscessfully"}, 200)
        else:
            return createResponse({"message": "Nothing to update"}, 200)
    except Exception as ex:
        print(ex)
        return createResponse({"message": "ERROR updating patient"}, 500)

#############################################################
#Entrada del API para la eliminación de un paciente en la BD
#############################################################
@app.route("/deletePatient/<id>", methods=["DELETE"])
def delete_patient(id):
    try:
        counter = patient_service.delete(db,id)
        if (counter == 1):
            return createResponse({"message": "Patient deleted suscessfully"}, 200)
        else:
           return createResponse({"message": "Patient not found."}, 200)
    except Exception as ex:
        print(ex)
        return createResponse({"message": "ERROR deleting patient"}, 500)

############################################################################
#Entrada del API para la predicción de un paciente segun el modelo entrenado
############################################################################
@app.route("/predictCancer/<id>", methods=["GET"])
def predict_cancer(id):
    try:
        result = patient_service.getCancerPrediction(db,id)
        if (result[0] == 1):
            message = "The tumor will be benign. Congrats"
        else:
            message = "Sorry, the tumor will be malign."
        return createResponse( {"message": "Patient cancer prediction got suscessfully",
                 "result":  f"{message}"}, 200)
    except Exception as ex:
        print(ex)
        return createResponse({"message": "ERROR predicting cancer"}, 500)


#Run API
if __name__ == "__main__":
    app.run(port=80, debug=True)