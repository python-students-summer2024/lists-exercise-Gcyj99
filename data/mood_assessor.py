import datetime
from pathlib import Path

def assess_mood():
    mood_dict = {
        "happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1,
        "angry": -2,
    }

    file_path = Path("data/mood_diary.txt")
    file_path.parent.mkdir(exist_ok=True, parents=True)

    today = datetime.date.today()
    if file_path.exists():
        with open(file_path, "r") as file:
            for line in file:
                date_str = line.strip().split(":")[1]
                if date_str == str(today):
                    print("Mood already recorded for today.")
                    return

    while True:
        mood = input("How do you feel today? (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if mood in mood_dict:
            break
        print("Invalid mood. Please enter one of the following: happy, relaxed, apathetic, sad, angry")

    with open(file_path, "a") as file:
        file.write(f"{mood}:{today}\n")

    print("Mood recorded. Thank you!")

    diagnose_mood(file_path, mood_dict)

def diagnose_mood(file_path, mood_dict):
    mood_scores = []
    today = datetime.date.today()
    seven_days_ago = today - datetime.timedelta(days=7)

    if file_path.exists():
        with open(file_path, "r") as file:
            for line in file:
                mood, date_str = line.strip().split(":")
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if seven_days_ago <= date <= today:
                    mood_scores.append(mood_dict[mood])

    if len(mood_scores) < 7:
        print("Not enough data to diagnose. Record your mood daily for a week.")
        return

    avg_score = sum(mood_scores) / len(mood_scores)
    if avg_score >= 1:
        print("Diagnosis: Manic")
    elif avg_score <= -1:
        print("Diagnosis: Depressive")
    else:
        print("Diagnosis: Normal")