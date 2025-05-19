# voice_ai_server.py
from flask import Flask, request, jsonify
import openai

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route("/listen", methods=["POST"])
def listen_and_process():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text received"}), 400

    print(f"📝 Text received: {text}")

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[{
                "role": "user",
                "content": f"What command is this dog owner saying? Just return one word like 'stand', 'sit', 'roll', 'shake' or 'playdead': {text}"
            }]
        )
        intent = response.choices[0].message.content.strip().lower()
        return jsonify({"command": intent})

    except Exception as e:
        print("❌ OpenAI error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5005)
