from fastapi import FastAPI, UploadFile, File, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import tensorflow as tf
import io

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the model
model = tf.saved_model.load('model/1/')


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    print("Received a frame")
    image = Image.open(io.BytesIO(await file.read()))
    image = np.array(image.resize((480, 480)), dtype=np.float32) / 255.0  # convert to float32
    prediction = model(image[np.newaxis, ...])

    # Get the index of the predicted class
    prediction_index = np.argmax(prediction)

    # Get the confidence of the prediction
    prediction_confidence = prediction[0][prediction_index]

    # Map the prediction to the correct class
    prediction_class = 'Biodegradable' if prediction_index == 0 else 'Non-Biodegradable'

    # Return a JSON object with 'prediction' and 'confidence' properties
    return {"prediction": prediction_class, "confidence": float(prediction_confidence) * 100}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            image = Image.open(io.BytesIO(data))
            image = np.array(image.resize((480, 480)), dtype=np.float32) / 255.0  # convert to float32
            prediction = model(image[np.newaxis, ...])
            prediction_index = np.argmax(prediction)
            prediction_confidence = prediction[0][prediction_index]
            prediction_class = 'Biodegradable' if prediction_index == 0 else 'Non-Biodegradable'
            await websocket.send_json({"prediction": prediction_class, "confidence": float(prediction_confidence) * 100})
    except WebSocketDisconnect:
        print("Client disconnected")
