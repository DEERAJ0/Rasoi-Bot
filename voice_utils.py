import time
import pyttsx3
import speech_recognition as sr
import streamlit as st

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_command(timeout=2):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            st.info("👂 Listening for command: say 'repeat' or 'exit'...")
            audio = recognizer.listen(source, timeout=timeout)
            command = recognizer.recognize_google(audio).lower()
            st.write(f"🗣️ You said: `{command}`")
            return command
        except sr.WaitTimeoutError:
            st.info("⏱️ No command heard. Continuing...")
            return None
        except Exception:
            st.warning("❌ Could not understand the command. Continuing...")
            return None

def speak_recipe_step_by_step(recipe):
    if not recipe:
        st.error("🚫 No recipe found.")
        return

    steps = [step.strip() for step in recipe.split('\n') if step.strip()]
    i = 0
    while i < len(steps):
        current_step = steps[i]
        st.markdown(f"**📝 Step {i+1}:** {current_step}")
        print(f"Step {i+1}: {current_step}")
        speak(current_step)

        command = recognize_command(timeout=2)

        if command == "repeat":
            continue  # stay on the same step
        elif command == "exit":
            speak("Okay, exiting recipe.")
            st.success("👋 Stopped reading recipe.")
            break
        else:
            i += 1  # move to next step
