import streamlit as st
from openrouter_api import get_recipe
from voice_utils import recognize_command, speak
from voice_utils import speak_recipe_step_by_step

st.set_page_config(page_title="🍳 Rasoi Bot")
st.title("👩‍🍳 Cooking Recipe Assistant")
st.markdown("Get recipes via **text or voice** input.")

input_mode = st.radio("Choose Input Mode", ["Text", "Voice"])

if input_mode == "Text":
    query = st.text_input("Enter the dish name:")
    if st.button("Get Recipe"):
        if query:
            recipe = get_recipe(query)
            st.text_area("Recipe", recipe, height=300)
            speak_recipe_step_by_step(recipe)

elif input_mode == "Voice":
    if st.button("🎙 Speak Dish Name"):
        query = recognize_command()
        st.write(f"You said: `{query}`")
        if query and "sorry" not in query.lower():
            recipe = get_recipe(query)
            st.text_area("Recipe", recipe, height=300)
            speak_recipe_step_by_step(recipe)
