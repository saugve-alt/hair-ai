def analyze_face(frame, model, session):
    """
    Uses YOLO model to detect face shape
    """

    results = model(frame, verbose=False)

    if not results:
        return

    # STUB: зараз просто фіксуємо форму
    face_shape = "square"

    if not session.has("face_shape"):
        session.set("face_shape", face_shape)
