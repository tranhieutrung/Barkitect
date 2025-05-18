# voice_ai_server.py
from flask import Flask, request, jsonify
import openai

client = openai.OpenAI(api_key="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")

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
