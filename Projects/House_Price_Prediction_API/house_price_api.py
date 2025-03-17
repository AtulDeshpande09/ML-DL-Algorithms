from flask import Flask, jsonify , request
import pandas as pd
import joblib

app = Flask(__name__)


def load_model():
    return joblib.load('Models/house_price_model.pkl')

model = load_model()

@app.route('/predict',methods=['POST'])
def predict(): 
    data = request.get_json(force=True)
    data_df = pd.DataFrame([data])
    prediction = model.predict(data_df)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
