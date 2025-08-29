import random
import os
import json

FILE = "quotes.json"

# Default mood quotes with 15 quotes each
mood_quotes = {
    "HAPPY": [
        "Happiness is not by chance, but by choice.",
        "A smile is the universal welcome.",
        "Joy is the simplest form of gratitude.",
        "Happiness is contagious — spread it.",
        "Count your age by friends, not years.",
        "Choose happiness daily.",
        "Happiness depends on ourselves.",
        "Happiness is homemade.",
        "Do more of what makes you happy.",
        "Happiness is a journey, not a destination.",
        "Find joy in the little things.",
        "Smile, it’s free therapy.",
        "Happiness grows when shared.",
        "Every day is a fresh start.",
        "Laugh more, worry less."
    ],
    "ANGER": [
        "Speak when you are angry — and you’ll make the best speech you’ll ever regret.",
        "Anger is one letter short of danger.",
        "For every minute you stay angry — you lose sixty seconds of peace.",
        "Holding on to anger is like drinking poison.",
        "Anger doesn’t solve anything.",
        "Stay calm, stay wise.",
        "Silence is the best reply to anger.",
        "Control your anger before it controls you.",
        "Peace is better than rage.",
        "Respond, don’t react.",
        "Let your anger go, embrace calm.",
        "Anger clouds judgment.",
        "Calm minds inspire solutions.",
        "Patience is strength.",
        "Breathe in peace, breathe out anger."
    ],
    "SAD": [
        "Tears are words the heart can’t say.",
        "Sadness flies away — on the wings of time.",
        "It’s okay — to not be okay.",
        "Every storm runs out of rain.",
        "This too shall pass.",
        "Behind every cloud is a silver lining.",
        "Sadness is but a wall between two gardens.",
        "Pain makes you stronger.",
        "Out of difficulties grow miracles.",
        "Don’t cry because it’s over, smile because it happened.",
        "Healing takes time.",
        "Sometimes you just need a good cry.",
        "Sadness adds depth to happiness.",
        "Darkness makes light shine brighter.",
        "Hope never leaves."
    ],
    "EXCITED": [
        "The best is yet to come!",
        "Excitement is contagious — spread it.",
        "Life begins — where comfort ends.",
        "Embrace the thrill of new beginnings.",
        "Stay curious, stay excited.",
        "Let your passion fuel your journey.",
        "Celebrate small victories.",
        "Anticipation makes life sweeter.",
        "Adventure is calling, answer it!",
        "Excitement sparks creativity.",
        "Be excited about today.",
        "Every sunrise brings new excitement.",
        "Keep chasing that thrill.",
        "Stay hyped, stay positive.",
        "Your energy attracts opportunities."
    ],
    "BORED": [
        "Boredom is the root of creativity.",
        "If you’re bored — you’re not paying attention.",
        "Boredom is simply — the desire for desires.",
        "Creativity cures boredom.",
        "Do something you’ve never tried.",
        "Bored? Read a book.",
        "Turn boredom into opportunity.",
        "Boredom is a blank canvas.",
        "Try learning something new.",
        "Invent, create, explore.",
        "Boredom fuels imagination.",
        "Silence boredom with passion.",
        "Bored? Write your own story.",
        "Boredom is a signal for change.",
        "Great ideas come from boredom."
    ],
    "LOVE": [
        "Love is all you need.",
        "Where there is love, there is life.",
        "Love conquers all.",
        "True love is endless.",
        "Spread love everywhere you go.",
        "Love is the greatest gift.",
        "To love and be loved is everything.",
        "Love is a language spoken by the heart.",
        "The best thing to hold onto is each other.",
        "Love never fails.",
        "Love grows when shared.",
        "Let love guide your actions.",
        "Love is patient, love is kind.",
        "Love heals all wounds.",
        "Love makes the world go round."
    ],
    "MOTIVATED": [
        "Push yourself, because no one else will.",
        "Dream it. Do it.",
        "Don’t stop until you’re proud.",
        "The harder you work, the luckier you get.",
        "Stay motivated, stay strong.",
        "Success is earned, not given.",
        "Wake up with determination.",
        "Great things never come from comfort zones.",
        "Work hard in silence, let success make the noise.",
        "Keep moving forward.",
        "Consistency beats talent.",
        "Your only limit is you.",
        "Stay hungry, stay foolish.",
        "Small steps lead to big results.",
        "Motivation is what gets you started, habit keeps you going."
    ],
    "STRESSED": [
        "Take a deep breath.",
        "Don’t stress over what you can’t control.",
        "Relax, refresh, recharge.",
        "Stress is temporary.",
        "Breathe in peace, breathe out stress.",
        "Don’t let stress steal your joy.",
        "One step at a time.",
        "Calm mind brings inner strength.",
        "Rest, and you’ll do your best.",
        "Let go of what weighs you down.",
        "Peace begins with a smile.",
        "Everything will be okay.",
        "Stress less, live more.",
        "Don’t carry tomorrow’s burden today.",
        "Self-care is not selfish."
    ],
    "CONFIDENT": [
        "Believe in yourself.",
        "Confidence is silent, insecurities are loud.",
        "Walk like you own the place.",
        "You are enough.",
        "Confidence breeds success.",
        "Be bold, be brave, be you.",
        "Shine without fear.",
        "Confidence is your best outfit.",
        "Own your story.",
        "Believe you can, and you’re halfway there.",
        "Confidence attracts opportunities.",
        "You’ve got this!",
        "Your vibe is your power.",
        "Confidence starts within.",
        "Doubt kills more dreams than failure."
    ],
    "TIRED": [
        "Rest is productive too.",
        "It’s okay to take a break.",
        "Sleep is the best meditation.",
        "Recharge to go further.",
        "Rest now, rise stronger.",
        "Even machines need to recharge.",
        "Don’t push past your limit.",
        "Listen to your body.",
        "Rest is part of success.",
        "Take it easy.",
        "A good rest is fuel for success.",
        "Tired today, stronger tomorrow.",
        "Balance is the key.",
        "Don’t burn out, shine bright.",
        "Relax, you deserve it."
    ],
    "INSPIRED": [
        "Be the change you wish to see in the world.",
        "Inspiration exists, but it has to find you working.",
        "Your story can inspire others.",
        "Dream big, start small.",
        "Turn your wounds into wisdom.",
        "Stay inspired, keep going.",
        "Everything you imagine is real.",
        "Your potential is limitless.",
        "Inspire before you expire.",
        "Light tomorrow with today.",
        "Creativity inspires progress.",
        "Your journey inspires others.",
        "Ideas are wings for the mind.",
        "Be an inspiration, not a follower.",
        "Stay inspired, stay alive."
    ]
}

# Load or create quotes file
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        quotes = json.load(f)
else:
    quotes = mood_quotes
    with open(FILE, "w") as f:
        json.dump(quotes, f, indent=2)

# Ensure new moods get added if missing
for mood, qlist in mood_quotes.items():
    if mood not in quotes:
        quotes[mood] = qlist

# Main loop
while True:
    print("\nWELCOME TO THE MOOD BASED QUOTE GENERATOR")
    print("CHOOSE FROM THE OPTIONS BELOW:")
    print("1 : ENTER YOUR MOOD FOR A QUOTE")
    print("2 : LIST ALL THE MOODS")
    print("3 : ADD A NEW QUOTE")
    print("4 : EXIT")

    choice = input("PLEASE ENTER AN OPTION (1-4): ")

    if choice == "1":
        mood = input("ENTER YOUR MOOD: ").strip().upper()
        if mood in quotes:
            print(f"\n👉 {random.choice(quotes[mood])}")
        else:
            print("⚠️ The mood you entered doesn't exist!")

    elif choice == "2":
        print("\nALL THE MOODS ARE:")
        for current_moods in quotes:
            print(f"- {current_moods}")

    elif choice == "3":
        new_mood = input("ENTER THE MOOD: ").strip().upper()
        new_quote = input("ENTER THE NEW QUOTE: ").strip()
        if new_mood in quotes:
            quotes[new_mood].append(new_quote)
        else:
            quotes[new_mood] = [new_quote]

        with open(FILE, "w") as f:
            json.dump(quotes, f, indent=2)

        print("✅ New quote has been added successfully!")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("⚠️ Invalid option, please try again!")
