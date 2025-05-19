import requests
import openai
import speech_recognition as sr

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("📝 You said:", text)

    response = requests.post("http://127.0.0.1:5005/listen", json={"text": text})
    data = response.json()

    command = data.get("command", "none").strip().lower()

    with open("command.txt", "w") as f:
        f.write(command)

except Exception as e:
    with open("command.txt", "w") as f:
        f.write("error")
