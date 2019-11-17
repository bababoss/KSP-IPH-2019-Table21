from flask import Flask, request, jsonify
import re
import pandas as pd
from flask_cors import CORS
import pickle


app = Flask(__name__)             # create an app instance
CORS(app)

@app.route("/", methods=['GET'])                   # at the end point /
def classify_severity():                      # call method hello 
    content = request.json
    df = pd.read_csv("/home/ubuntu/projects/police_hackathon/csv_file/accident_report_vehicle_merge.csv")
    df = df.loc[:1,['Collision_Type_val', 'Accident_Spot_val',
                   'Accident_Location_val', 'Junction_Control_val', 'Road_Character_val',
       'Road_Type_val', 'Road_Classification_val', 'Seperation_val',
       'Surface_Type_val', 'Surface_Condition_val', 'Road_Condition_val',
       'weather_val', 'Main_Cause_val', 'Hit_Run_val', 'Lane_Type_val',
       'Road_Markings_val', 'Spot_Conditions_val', 'Accident_Location_id_val',
       'RoadJunction_val', 'Accident_spotb_val','Vehicle_Type',
       'Vehicle_Vanoeuvre','Vehicle_Load','Fuel_Type',
       'Vehicle_Sub_Type']]
    
    
    df = pd.get_dummies(df, columns=['Collision_Type_val', 'Accident_Spot_val',
      'Accident_Locaaccident_vehicletion_val', 'Junction_Control_val', 'Road_Character_val',
      'Road_Type_val', 'Road_Classification_val', 'Seperation_val',
      'Surface_Type_val', 'Surface_Condition_val', 'Road_Condition_val',
      'weather_val', 'Main_Cause_val', 'Hit_Run_val', 'Lane_Type_val', 'Road_Markings_val',
      'Spot_Conditions_val', 'Accident_Location_id_val',
      'RoadJunction_val', 'Accident_spotb_val'])
    
    X_new = pd.get_dummies(df, columns=['Vehicle_Type', 'Vehicle_Vanoeuvre', 'Vehicle_Load', 'Fuel_Type','Vehicle_Sub_Type'])
    return loaded_model.predict(X_new)
    
    
       
    
if __name__ == "__main__":
    # on running python app.py
    filename = '/home/ubuntu/projects/police_hackathon/Severity_Classification/severity_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    app.run(host='0.0.0.0',port='8097')
    
