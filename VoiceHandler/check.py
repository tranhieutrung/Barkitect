import openai

client = openai.OpenAI(api_key="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")

# Gọi endpoint usage để lấy thông tin quota
usage = openai.Usage.retrieve()

print(usage)
