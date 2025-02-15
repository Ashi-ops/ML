import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import random
import pyttsx3
import requests
import speech_recognition as sr
from PIL import Image, ImageTk
import time
import threading

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def use_microphone():
    """Capture input from the microphone using speech recognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
        except Exception as e:
            speak(f"An error occurred: {e}")
    return ""

def open_notepad():
    """Open Notepad."""
    os.system("notepad")
    speak("Notepad is now open. Let's get to work!")

def open_website():
    """Open a website."""
    website = website_entry.get()
    if not website:
        speak("Please say the name of the website.")
        website = use_microphone()
    
    if website:
        if not website.startswith("http"):
            website = "https://" + website
        webbrowser.open(website)
        speak(f"Opening {website}.")
    else:
        speak("No website provided.")

def perform_google_search():
    """Search Google."""
    query = google_entry.get()
    if not query:
        speak("Please say what you want to search for.")
        query = use_microphone()
    
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query} on Google.")
    else:
        speak("No search query provided.")

def tell_a_joke():
    """Tell a joke and show confetti."""
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why did the math book look sad? Because it had too many problems.",
        "What’s orange and sounds like a parrot? A carrot!",
        "Why don’t eggs tell jokes? Because they might crack up!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "Why do bees have sticky hair? Because they use honeycombs!",
        "Why don’t oysters donate to charity? Because they are shellfish!",
        "Why was the computer cold? It left its Windows open!",
        "What do you call cheese that isn’t yours? Nacho cheese!",
        "Why can’t your nose be 12 inches long? Because then it would be a foot!",
        "Why don’t elephants chew gum? They do, just not in public!",
        "Why don’t some couples go to the gym? Because some relationships don’t work out!",
        "Why did the cookie go to the hospital? Because it felt crumby!",
        "Why was the math book sad? Because it had too many problems!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why don’t crabs give to charity? Because they’re shellfish!",
        "Why was the stadium so cold? Because it was filled with fans!",
        "Why do cows wear bells? Because their horns don’t work!",
        "Why was the belt arrested? It held up a pair of pants!",
        "Why do bananas never get lonely? Because they hang out in bunches!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why don’t you ever see elephants hiding in trees? Because they’re so good at it!",
        "What do you call a factory that makes okay products? A satisfactory!",
        "What’s a ninja’s favorite type of shoe? Sneakers!",
        "Why don’t vampires attack Taylor Swift? Because she has bad blood!",
        "Why can’t you give Elsa a balloon? Because she’ll let it go!"
    ]
    joke = random.choice(jokes)
    joke_label.config(text=joke)
    speak(joke)
    show_confetti()

def show_confetti():
    """Simulate confetti by changing the background color."""
    global random_bg
    new_color = random.choice(colors)
    while new_color == random_bg:  # Ensure the new color is different
        new_color = random.choice(colors)
    random_bg = new_color
    root.config(bg=random_bg)
    title_label.config(bg=random_bg)
    website_label.config(bg=random_bg)
    google_label.config(bg=random_bg)
    joke_label.config(bg=random_bg)
    fact_label.config(bg=random_bg)
    weather_label.config(bg=random_bg)
    weather_result.config(bg=random_bg)

def show_fun_fact():
    """Show a fun fact and display confetti."""
    facts = [
        "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
        "Did you know? Octopuses have three hearts!",
        "Did you know? A group of flamingos is called a flamboyance.",
        "Did you know? The world’s smallest reptile was discovered in 2021 in Madagascar, and it fits on a fingertip.",
        "Did you know? Bananas are berries, but strawberries aren’t!",
        "Did you know? Wombat poop is cube-shaped.",
        "Did you know? An ostrich’s eye is bigger than its brain.",
        "Did you know? There’s only one letter that doesn’t appear in any U.S. state name: Q.",
        "Did you know? A snail can sleep for three years at a time.",
        "Did you know? The heart of a blue whale weighs about as much as a car.",
        "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
        "Did you know? Some cats are allergic to humans!",
        "Did you know? Sea otters hold hands when they sleep to keep from drifting apart.",
        "Did you know? There are more stars in the universe than grains of sand on Earth.",
        "Did you know? Cows have best friends and can get stressed when separated.",
        "Did you know? The inventor of the frisbee was turned into a frisbee after he died.",
        "Did you know? A cloud can weigh over a million pounds.",
        "Did you know? The majority of your brain is fat.",
        "Did you know? Sloths can hold their breath longer than dolphins can.",
        "Did you know? Koalas have fingerprints just like humans!",
        "Did you know? There’s a basketball court on the top floor of the U.S. Supreme Court Building, known as the Highest Court in the Land.",
        "Did you know? Water makes different pouring sounds depending on its temperature.",
        "Did you know? The dot over a lowercase \"i\" or \"j\" is called a tittle.",
        "Did you know? Tigers have striped skin, not just striped fur.",
        "Did you know? Apples float because they’re 25% air.",
        "Did you know? The tongue of a blue whale weighs as much as an elephant.",
        "Did you know? A group of porcupines is called a prickle.",
        "Did you know? Butterflies taste with their feet.",
        "Did you know? The longest hiccuping spree lasted 68 years.",
        "Did you know? You’re more likely to get stung by a bee when it’s windy." 
    ]
    fact = random.choice(facts)
    fact_label.config(text=fact)
    speak(fact)
    show_confetti()

def get_weather():
    """Fetch and display weather information for the entered city."""
    city = weather_entry.get().strip()
    if not city:
        speak("Please enter a city name.")
        return

    api_key = "c3762047336ea07bc7fea9a0bff66db7"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            message = f"The weather in {city} is {weather}. The temperature is {temperature}°C and humidity is {humidity}%."
            weather_result.config(text=message)
            speak(message)
        else:
            error_message = f"Error: {data['message']}"
            weather_result.config(text=error_message)
            speak(error_message)
    except Exception as e:
        weather_result.config(text=f"An error occurred: {e}")
        speak("An error occurred while fetching the weather.")

# Randomize colors
colors = ["#FF6347", "#FFD700", "#32CD32", "#1E90FF", "#EE82EE", "#FFA500", "#00CED1", "#FF69B4"]
random_bg = random.choice(colors)
random_fg = "#FFFFFF" if random_bg in ["#FF6347", "#FFD700", "#FFA500", "#FF69B4"] else "#000000"

# Create the main application window
root = tk.Tk()
root.title("Ashi's Interactive Assistant")
root.geometry("700x800")
root.config(bg=random_bg)

# Fun Title
title_label = tk.Label(root, text="🌟 Ashi's Interactive Assistant 🌟", font=("Helvetica", 24, "bold"), fg=random_fg, bg=random_bg)
title_label.pack(pady=20)

# Website Section
website_label = tk.Label(root, text="🌐 Enter Website or Speak:", font=("Arial", 14), bg=random_bg, fg=random_fg)
website_label.pack(pady=10)
website_entry = tk.Entry(root, width=40, font=("Arial", 14))
website_entry.pack(pady=10)
website_button = tk.Button(root, text="Open Website", font=("Arial", 12, "bold"), bg="#FF5722", fg="white", command=open_website)
website_button.pack(pady=10)

# Google Search Section
google_label = tk.Label(root, text="🔎 Enter Google Query or Speak:", font=("Arial", 14), bg="#222831", fg="#EEEEEE")
google_label.pack(pady=10)
google_entry = tk.Entry(root, width=40, font=("Arial", 14))
google_entry.pack(pady=10)
google_button = tk.Button(root, text="Search Google", font=("Arial", 12, "bold"), bg="#FF5722", fg="white", command=perform_google_search)
google_button.pack(pady=10)

# Joke Section
joke_label = tk.Label(root, text="", font=("Arial", 14), bg="#222831", fg="#FFD369", wraplength=600)
joke_label.pack(pady=10)
joke_button = tk.Button(
    root,
    text="Tell Me a Joke",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=lambda: [tell_a_joke(), show_confetti()]
)
joke_button.pack(pady=10)

# Fact Section
fact_label = tk.Label(root, text="", font=("Arial", 14), bg="#222831", fg="#FFD369", wraplength=600)
fact_label.pack(pady=10)
fact_button = tk.Button(
    root,
    text="Say a Fact",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=lambda: [show_fun_fact(), show_confetti()]
)
fact_button.pack(pady=10)

# Weather Section
weather_label = tk.Label(root, text="☁️ Enter City for Weather Info:", font=("Arial", 14), bg="#222831", fg="#EEEEEE")
weather_label.pack(pady=10)
weather_entry = tk.Entry(root, width=40, font=("Arial", 14))
weather_entry.pack(pady=10)
weather_button = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=get_weather)
weather_button.pack(pady=10)
weather_result = tk.Label(root, text="", font=("Arial", 14), bg="#222831", fg="#FFD369", wraplength=600)
weather_result.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="#FF0000", fg="white", command=root.quit)
exit_button.pack(pady=20)

# Run the main loop
root.mainloop()