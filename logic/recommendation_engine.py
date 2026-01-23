def generate_recommendations(session):
    recs = []

    face = session.get("face_shape")
    hair_data = session.get("hair_data", {})
    hair_type = hair_data.get("hair_type", "unknown")
    problems = hair_data.get("problems", {})

    # ---- ФОРМА ОБЛИЧЧЯ ----
    if face == "round":
        recs.append("Підійдуть стрижки з обʼємом зверху та короткими боками")
    elif face == "square":
        recs.append("Рекомендуються мʼякі переходи та текстурований верх")
    elif face == "oval":
        recs.append("Овальна форма — універсальна, підходить більшість стилів")

    # ---- ТИП ВОЛОССЯ ----
    if hair_type == "curly":
        recs.append("Рекомендується догляд для кучерявого волосся (curl cream)")
    elif hair_type == "wavy":
        recs.append("Підійдуть легкі текстурні засоби")
    elif hair_type == "straight":
        recs.append("Можна використовувати матові пасти або пудру")
    elif hair_type == "unknown":
        recs.append("Тип волосся визначено неточно — рекомендації загальні")

    # ---- ПРОБЛЕМИ ----
    if "dandruff" in problems:
        recs.append("Рекомендовано шампуні проти лупи")
    if "hair_loss" in problems:
        recs.append("Варто звернути увагу на випадіння волосся")
    if "oily" in problems:
        recs.append("Рекомендується контроль жирності шкіри голови")
    if "dry" in problems:
        recs.append("Потрібен зволожуючий догляд")

    # ---- ЗАГАЛЬНЕ ----
    recs.append("Регулярна корекція стрижки кожні 4–6 тижнів")

    return recs
