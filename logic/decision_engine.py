from logic.question_engine import ask_question
from logic.recommendation_engine import generate_recommendations


QUESTIONS = [
    (
        "style_pref",
        "Оберіть стиль, який вам ближчий:",
        ["Чоловічий", "Жіночий", "Універсальний"]
    ),
    (
        "hair_length",
        "Яку довжину волосся ви зазвичай носите?",
        ["Коротку", "Середню", "Довгу"]
    ),
    (
        "scalp_condition",
        "Як би ви оцінили стан шкіри голови?",
        ["Комфортний", "Іноді дискомфорт", "Чутлива"]
    )
]


def decide_next_action(session):
    # -------- ПИТАННЯ --------
    for key, text, options in QUESTIONS:
        if not session.has(key):
            ans = ask_question(session, key, text, options)
            if ans:
                session.set(key, ans)
            return

    # -------- ФІНАЛ --------
    if not session.is_finished():
        recs = generate_recommendations(session)

        print("\n📌 РЕКОМЕНДАЦІЇ:")
        for r in recs:
            print("•", r)

        session.finish()
