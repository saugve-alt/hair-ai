from fastapi import FastAPI
from ultralytics import YOLO

app = FastAPI()

model = None

@app.on_event("startup")
def load_model():
    global model
    model = YOLO("yolov8n-cls.pt")  # або твій .pt
    print("YOLO loaded")

@app.get("/")
def root():
    return {"status": "ok"}
