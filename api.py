from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO
import numpy as np
import cv2
import os

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLO model
model = YOLO("yolov10n.pt")
print("Classes loaded:", model.names)

# Templates folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Serve static files (CSS, JS, videos)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Serve homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# YOLO detection endpoint
@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img_arr = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    results = model(frame, conf=0.25, iou=0.5)

    detections = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        label = results[0].names[int(box.cls[0])]
        conf = float(box.conf[0])
        detections.append({
            "label": label,
            "confidence": conf,
            "box": [x1, y1, x2, y2]
        })

    return {"detections": detections}
