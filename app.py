# Import python dependencies | libraries
import uvicorn
import joblib
import pickle, json
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from HousePriceDeploy import HousePrice

# Instantiate the app object
app = FastAPI()

# Load model
with open("model_rfc.pkl","rb") as file:
    model = pickle.load(file)

# Define the prediction route
@app.post('/predict')
async def predict_price(data: HousePrice):
    # Extract input features from the request
    df = pd.DataFrame([data.dict()])
    
    # Make prediction
    predict_price = model.predict(df)
    
    # Return the prediction as JSON response
    return {"predict_price":predict_price[0]}
  
  
  # Launch the FastAPI server
if __name__ == '__main__':
    # Import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, reload_excludes=False)  

    
