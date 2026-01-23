def detect_hair_type(detections):
    """
    Визначає тип волосся на основі детекцій YOLO.
    Повертає: curly | wavy | straight | unknown
    """

    counts = {
        "curly": 0,
        "wavy": 0,
        "straight": 0
    }

    for d in detections:
        cls = d.get("class")
        conf = d.get("confidence", 0)

        if conf < 0.5:
            continue

        if cls in counts:
            counts[cls] += 1

    if all(v == 0 for v in counts.values()):
        return "unknown"

    return max(counts, key=counts.get)
