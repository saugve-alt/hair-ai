from hair.hair_type import detect_hair_type
from hair.hair_check import detect_hair_problems


def analyze_hair(detections):
    """
    Агрегує результат аналізу волосся
    """

    return {
        "hair_type": detect_hair_type(detections),
        "problems": detect_hair_problems(detections)
    }
