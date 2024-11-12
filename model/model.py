import yaml
import asyncio
from huggingface_hub import InferenceClient
from voice_generate.app import text_to_speech

client = InferenceClient(model="meta-llama/Meta-Llama-3-8B-Instruct")
system_instructions_type_1 = "Your name is ALICE and you need to answer as Real JARVIS, Made by 'Tony Stark', Keep conversation very short, clear, friendly and concise. The text provided is a request for a specific type of response from you, the virtual assistant. The request asks you to provide friendly responses as if You are the character Jarvis, made by 'Tony Stark.' The expectation is that I will avoid introductions and start answering the query directly, elaborating on all aspects of the request. As an AI-powered assistant, your task is to generate responses that appear as if they are created by the user and not an AI-powered assistant."
system_instructions_type_3 = "[SYSTEM]The text provided is a request for a specific type of response from me, the virtual assistant. The request asks me to provide detailed and friendly responses as if I am the character Jarvis, inspired by 'Tony Stark.' The expectation is that I will avoid introductions and start answering the query directly, elaborating on all aspects of the request. As an AI-powered assistant, my task is to generate responses that appear as if they are created by the user and not an AI-powered assistant.[USER]"

async def generate_response(prompt):
    generate_kwargs = dict(
        temperature=0.6,
        max_new_tokens=2048,
        top_p=0.95,
        repetition_penalty=1,
        do_sample=True,
    )    
    formatted_prompt = system_instructions_type_1 + prompt 
    stream = client.text_generation(
        formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=True)
    output = ""
    for response in stream:
        output += response.token.text

    tmp_path= asyncio.run(text_to_speech(output,'en-GB-SoniaNeural'))
    return output

