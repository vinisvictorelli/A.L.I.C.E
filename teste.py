from huggingface_hub import InferenceClient

client = InferenceClient(model="meta-llama/Meta-Llama-3-8B-Instruct")

# Assuming the model supports text generation
output = client.text_generation(prompt="Who is albert einstein?")
print(output)
print(type(output))