def ask_question(session, key, text, options):
    """
    Питає користувача ТІЛЬКИ якщо значення ще нема.
    Працює через термінал (CLI).
    """

    if session.has(key):
        return None

    print(f"\n❓ {text}")
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")

    try:
        choice = int(input("Ваш вибір: ").strip())
        if 1 <= choice <= len(options):
            return options[choice - 1]
    except ValueError:
        pass

    return None
