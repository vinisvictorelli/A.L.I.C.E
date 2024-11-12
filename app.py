import gradio as gr
import asyncio
from model.model import generate_response
from voice_recognition.app import reconhecimento_audio

DESCRIPTION = """
<center><h1>ALICE created by Vinicius Victorelli</h1></center>
### <center>A.L.I.C.E is a personal Assistant that uses a series of llm's to process text input from the user and produce a response as voice output</center>
"""

with gr.Blocks(css="style.css") as demo:

    gr.Markdown(DESCRIPTION)
    
    # Area para o histórico de mensagens
    with gr.Column(elem_id="chat_history_container"):
        chat_history = gr.Chatbot(label="Chat History", elem_id="chat_history")

    # Barra de entrada do usuário na parte inferior
    with gr.Row(variant="panel", elem_id="input_row"):
        user_input = gr.Textbox(
            placeholder="Type your question here...",
            elem_id="user_input",
            show_label=False,
            lines=1,
            scale= 8
        )

        # Ícones de microfone e upload na barra de entrada
        mic_icon = gr.Button(value="🎤", elem_id="mic_icon",scale=1)
        upload_icon = gr.Button(value="📁", elem_id="upload_icon",scale=1)

    # Funções para manipular as mensagens e os botões de áudio/upload
    def handle_user_message(text, history):
        # Função de resposta do modelo
        response = asyncio.run(generate_response(text))
        # Adiciona as mensagens ao histórico
        history.append((text, response))
        return history, "", response

    # Integração dos componentes na interface
    mic_icon.click(
        fn=reconhecimento_audio,  # Função para gravar áudio
        inputs=[],
        outputs=user_input
    )

    upload_icon.click(
        fn=lambda x: x,  # Função para upload de arquivo
        inputs=[user_input],
        outputs=user_input
    )

    user_input.submit(
        fn=handle_user_message,
        inputs=[user_input, chat_history],
        outputs=[chat_history, user_input]
    )

if __name__ == "__main__":
    demo.queue(max_size=200).launch()
