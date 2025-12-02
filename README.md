# Real-Time Object Detection with FastAPI & YOLO

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-lightgrey)](https://fastapi.tiangolo.com/)  
[![YOLO](https://img.shields.io/badge/YOLO-YOLOv10n-orange)](https://github.com/ultralytics/ultralytics)  
[![License](https://img.shields.io/badge/License-MIT-green)](https://chatgpt.com/c/LICENSE)

A **real-time object detection system** that leverages **YOLOv10n** for high-performance object detection and **FastAPI** as the backend. The interactive web frontend allows users to detect objects live from their webcam. The application also includes demo videos showcasing the detection capabilities.

----------

## 🚀 Features

-   Real-time object detection via webcam.
    
-   Powered by **YOLOv10n** for fast and accurate detection.
    
-   Interactive frontend with live bounding boxes.
    
-   Demo videos included for testing detection.
    
-   Fully responsive UI with modern design.
    
-   Easy to extend for new models or additional functionality.
    

----------

## 📁 Project Structure

```
project_folder/
├─ api.py                    # FastAPI backend
├─ yolov10n.pt               # YOLO pretrained model
├─ templates/
│   └─ index.html            # Frontend HTML page
├─ static/
│   ├─ videos/
│   │   ├─ new_video.mp4
│   │   └─ Real_Time_Object_Detection.mp4
│   ├─ css/                  # Optional external CSS
│   │   └─ style.css
│   └─ js/                   # Optional external JS
│       └─ script.js

```

> Videos must be placed inside `static/videos/` to prevent 404 errors.

----------

## ⚙️ Prerequisites

-   Python 3.10+
    
-   pip
    
-   Modern web browser (Chrome, Firefox, Edge)
    

----------

## 🛠️ Installation

1.  **Clone the repository:**
    

```bash
git clone <repo-url>
cd project_folder

```

2.  **Create a virtual environment (recommended):**
    

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

```

3.  **Install dependencies:**
    

```bash
pip install fastapi uvicorn numpy opencv-python ultralytics jinja2

```

----------

## 🏃 Running the Application

Start the FastAPI server:

```bash
uvicorn api:app --reload

```

Open your browser and navigate to:

```
http://127.0.0.1:8000/

```

-   Click **Start Camera** to begin real-time object detection.
    
-   Click **Stop Camera** to stop the webcam feed.
    
-   Demo videos are available under the **Sample Outputs** section.
    

----------

## 📡 API Endpoints

### **POST /detect**

-   **Description:** Detect objects in an uploaded image.
    
-   **Request:** `multipart/form-data` with key `file` containing the image.
    
-   **Response:**
    

```json
{
  "detections": [
    {
      "label": "person",
      "confidence": 0.98,
      "box": [x1, y1, x2, y2]
    },
    ...
  ]
}

```

> The frontend automatically posts each video frame to this endpoint for live detection.

----------

## 🖥️ Frontend Notes

-   HTML page is in `templates/index.html`.
    
-   CSS, JS, videos, and other assets are served via FastAPI static route `/static`.
    
-   For clean code maintenance, CSS and JS can be moved to external files in `static/css/` and `static/js/`.
    

----------

## 📌 Recommended Improvements

-   Use external JS/CSS files to make the HTML cleaner.
    
-   Use HTTPS for accessing the webcam in production environments.
    
-   Deploy using **Gunicorn** or **Uvicorn with multiple workers** for production.
    
-   Add more YOLO models for custom detection scenarios.
    
-   Include logging and error handling for production readiness.
    

----------

## 🎨 Demo

![Demo GIF Placeholder](https://via.placeholder.com/800x400?text=Real-Time+Object+Detection+Demo)

----------

## 👨‍💻 Author

**Eswar Potti**

-   [GitHub](https://github.com/eswarpotti3)
    
-   [LinkedIn](https://www.linkedin.com/in/eswar-potti)
    

----------

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.