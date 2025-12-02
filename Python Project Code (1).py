# ------------------------------
# Typing Speed & Accuracy Analyzer
# ------------------------------
import time, random, csv, os
from colorama import Fore, Style, init
init(autoreset=True)

# ------------------------------
# Sentence banks (levels)
# ------------------------------
EASY = [
    "Python is fun to learn",
    "Practice makes perfect",
    "Coding improves thinking"
]

MEDIUM = [
    "Debugging teaches patience and focus",
    "Programming improves logical skills",
    "Errors are part of the learning process"
]

HARD = [
    "Artificial intelligence transforms industries rapidly",
    "Consistency beats talent when talent does not work hard",
    "Data structures and algorithms form the core of computing"
]

# ------------------------------
# Helper functions
# ------------------------------

def choose_level():
    print(Fore.CYAN + "\nChoose difficulty level:")
    print("1. Easy\n2. Medium\n3. Hard")
    ch = input("Enter your choice (1/2/3): ").strip()
    if ch == "1":   return "Easy", EASY
    if ch == "2":   return "Medium", MEDIUM
    if ch == "3":   return "Hard", HARD
    print(Fore.RED + "Invalid choice, defaulting to Easy.")
    return "Easy", EASY

def calculate_accuracy(original, typed):
    correct = sum(1 for i, c in enumerate(typed)
                  if i < len(original) and c == original[i])
    return round((correct / len(original)) * 100, 2)

def save_score(name, level, speed, accuracy):
    """Appends a record to leaderboard.csv"""
    with open("leaderboard.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, level, speed, accuracy])

def show_leaderboard():
    print(Fore.YELLOW + "\n----- Leaderboard -----")
    if not os.path.exists("leaderboard.csv"):
        print("No records yet.")
        return
    with open("leaderboard.csv") as f:
        for row in csv.reader(f):
            print(f"{row[0]:10} | {row[1]:7} | {row[2]} WPM | {row[3]} %")

# ------------------------------
# Main typing logic
# ------------------------------
def typing_test(name, level_name, sentences):
    sentence = random.choice(sentences)
    print(Fore.CYAN + "\nType this sentence:\n" + Fore.WHITE + sentence)
    input(Fore.MAGENTA + "\nPress Enter when ready...")
    start = time.time()
    typed = input(Fore.GREEN + "\nStart typing here:\n" + Fore.RESET)
    end = time.time()

    elapsed = round(end - start, 2)
    words = len(sentence.split())
    speed = round((words / elapsed) * 60, 2)
    accuracy = calculate_accuracy(sentence, typed)

    # show color-coded difference
    print("\nYour typing result:")
    for i, c in enumerate(typed):
        if i < len(sentence) and c == sentence[i]:
            print(Fore.GREEN + c, end="")
        else:
            print(Fore.RED + (c if i < len(sentence) else ""), end="")
    print(Style.RESET_ALL)

    print(f"\nTime Taken: {elapsed}s")
    print(f"Speed: {speed} WPM")
    print(f"Accuracy: {accuracy}%")

    # small motivational message
    if accuracy >= 90:
        print(Fore.GREEN + "Excellent typing!")
    elif accuracy >= 70:
        print(Fore.YELLOW + "Good effort, keep practicing!")
    else:
        print(Fore.RED + "Needs improvement, practice more!")

    save_score(name, level_name, speed, accuracy)

# ------------------------------
# Application menu
# ------------------------------
def main():
    print(Fore.CYAN + "\n=== Typing Speed & Accuracy Analyzer ===")
    name = input("Enter your name: ").strip().title() or "Guest"

    while True:
        print(Fore.MAGENTA + "\nMenu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            level_name, sentences = choose_level()
            typing_test(name, level_name, sentences)
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print(Fore.CYAN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")

# ------------------------------
# Run program
# ------------------------------
if __name__ == "__main__":
    main()
