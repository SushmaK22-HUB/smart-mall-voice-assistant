import pyttsx3
import threading

def _run_tts(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("TTS Error:", e)

def speak(text):
    if not text or not text.strip():
        return
    # Clean up markdown formatting symbols before speaking
    clean_text = text.replace("•", "").replace("*", "").replace("#", "").replace("🏬", "").replace("🍔", "").replace("📍", "")
    
    # If the text is a huge list, speak a concise friendly summary
    if len(clean_text) > 180:
        clean_text = clean_text[:160] + "... and more options are shown on your screen."
        
    # Run audio in a background thread so Streamlit UI displays instantly without lag
    threading.Thread(target=_run_tts, args=(clean_text,), daemon=True).start()