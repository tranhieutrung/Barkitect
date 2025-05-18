import requests
import openai
import speech_recognition as sr

client = openai.OpenAI(api_key="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")

# print("🎤 Speak a command after pressing Enter")
# input("Press Enter to record...")


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
