import numpy
import pandas
import pickle 
import sklearn
from flask import Flask, render_template, request


with open("Predict_Insurance_Cost_MLmodel.pickle", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

#API endpoint
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/ping")
def ping():
    return {"message ": "Hey there ...!"}


@app.route("/submit", methods = ["GET", "POST"])
def submit_form():
    if request.method == "GET":
        return ("I will make the prediction for Insurance Price!, Thanks for visiting the website :)")
    else:
        #post request along with the data
        #ins_req = request.get_json()
        #age = ins_req["Age"]
                  
        age = int(request.form.get("age", 0))
        

        diabetes = request.form.get("diabetes")
        if diabetes == "Yes":
            diabetes = 1
        else:
            diabetes = 0
        print(diabetes, flush=True)


        bp = request.form.get("bp")
        if bp == "Yes":
            bp = 1
        else:
            bp = 0
        print(bp, flush=True)


        transplants = request.form.get("transplants")
        if transplants == "Yes":
            transplants = 1
        else:
            transplants = 0
        print(transplants, flush=True)


        disease = request.form.get("disease")
        if disease == "Yes":
            disease = 1
        else:
            disease = 0
        print(disease, flush=True)

        height = int(request.form.get("height",0))
        weight = int(request.form.get("weight",0))

        allergy = request.form.get("allergy")
        if allergy == "Yes":
            allergy = 1
        else:
            allergy = 0
        print(allergy, flush=True)



        cancer = request.form.get("cancer")
        if cancer == "Yes":
            cancer = 1
        else:
            cancer = 0
        print(cancer, flush=True)


        surgery = int(request.form.get("surgery",0))    



        input_data = [age, diabetes, bp, transplants, disease, height, weight, allergy, cancer, surgery]

        print(input_data, flush=True)

        result = model.predict([input_data])
        print(result, flush=True)

        '''
        #return {"Predicted Insurance Price": round(result[0],0)}
        '''

        cont = {
            "age": age,
            "diabetes": diabetes,
            "bp": bp,
            "transplants": transplants,
            "disease": disease,
            "height": height,
            "weight": weight,
            "allergy": allergy,
            "cancer": cancer,
            "surgery": surgery,
            "prediction": result[0]


        }   

        print("Rendering result.html..", flush=True)
        return render_template("result.html", **cont) 
        
                     

    