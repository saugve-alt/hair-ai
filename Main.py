from ultralytics import YOLO
from camera_live import run_camera
from logic.session_state import SessionState


def main():
    model = YOLO(
        r"C:\Users\Voiev\PyCharmMiscProject\.venv\runs_faceshape\faceshape_finetune\weights\best.pt"
    )

    session = SessionState()   # ← ОДИН ОБʼЄКТ НА ВСЮ СЕСІЮ

    run_camera(model, session)


if __name__ == "__main__":
    main()
