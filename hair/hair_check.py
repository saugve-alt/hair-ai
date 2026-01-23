def detect_hair_problems(detections, threshold=2):
    """
    Рахує підтверджені проблеми волосся / шкіри голови.
    threshold — мінімальна кількість детекцій для підтвердження
    """

    counters = {
        "dandruff": 0,
        "oily": 0,
        "dry": 0,
        "hair_loss": 0
    }

    for d in detections:
        cls = d.get("class")
        conf = d.get("confidence", 0)

        if conf < 0.5:
            continue

        if cls in counters:
            counters[cls] += 1

    return {
        k: v for k, v in counters.items() if v >= threshold
    }
