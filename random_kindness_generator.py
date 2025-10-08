import random
import time

messages = [
    "💜 You are doing great — one commit at a time!",
    "✨ Keep coding, keep growing!",
    "🌍 Your contribution makes open source more inclusive.",
    "🚀 Every PR counts — keep pushing forward!",
    "🌸 Kindness is contagious. Spread it through your code!",
    "💪 Believe in yourself — the world needs your ideas."
]

def kindness_boost():
    print("\n🌟 Welcome to the SHEROS × ACM-W Kindness Generator 🌟\n")
    time.sleep(1)
    for _ in range(3):
        msg = random.choice(messages)
        print(msg)
        time.sleep(1)

if __name__ == "__main__":
    kindness_boost()
