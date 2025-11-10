from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import numpy as np
import cv2

app = FastAPI()

# Allow website → backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLOv10n (same as your local script)
model = YOLO("yolov10n.pt")
print("Classes loaded:", model.names)

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img_arr = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    # Run detection with confidence threshold lowered to detect small objects
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
