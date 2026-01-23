import base64
import cv2
import numpy as np

from hair.hair_analyzer import analyze_hair
from logic.decision_engine import decide_next_action


def run_camera(model, session, frame_b64=None):
    """
    Якщо frame_b64 == None → режим заглушки (нічого не ламає)
    Якщо frame_b64 є → обробка кадру з браузера
    """

    if frame_b64 is None:
        return

    # ---- base64 → image ----
    img_bytes = base64.b64decode(frame_b64.split(",")[1])
    np_arr = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # ---- YOLO ----
    results = model(frame, verbose=False)

    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "class": model.names[int(box.cls)],
                "confidence": float(box.conf)
            })

    # ---- HAIR ANALYSIS ----
    hair_data = analyze_hair(detections)
    session.set("hair_data", hair_data)

    # ---- FLOW ----
    decide_next_action(session)

    return {
        "hair": hair_data,
        "session": session.dump()
    }
