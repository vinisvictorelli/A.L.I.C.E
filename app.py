import os
import re
import gradio as gr
import edge_tts
import asyncio
import time
import tempfile
from huggingface_hub import InferenceClient
from voice_generate.app import text_to_speech
from model.llm import generate_response
from voice_recognition.app import reconhecimento_audio

DESCRIPTION = """ # <center><h1>ALICE created by Vinicius Victorelli</h1></center>
        ### <center>A.L.I.C.E is a personal Assistant that uses a series of llm's to proccess the text input from the user and produce a response as a voice output</center>
        """

with gr.Blocks(css="style.css") as demo:
    
  gr.Markdown(DESCRIPTION)

  with gr.Row():
    user_input = gr.TextArea(label="Ask A.L.I.C.E.", placeholder="Type your question here", elem_id="user_input")
    voice_input = gr.Audio(sources=["microphone"])
  with gr.Row():
    ask_button = gr.Button("Ask", elem_classes="ask-button")  # Add class for styling
  with gr.Row():
    response_area = gr.Textbox(label="A.L.I.C.E.'s Response", value="", elem_id="response")
    output_audio = gr.Audio(label="A.L.I.C.E's Voice", type="filepath",
                        interactive=False,
                        autoplay=True,
                        elem_classes="audio")
    
  ask_button.click(fn=generate_response, inputs=user_input, outputs=[response_area,output_audio], api_name="translate")

if __name__ == "__main__":
    demo.queue(max_size=200).launch()
