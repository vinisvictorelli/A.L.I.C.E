import edge_tts
import asyncio
import tempfile


async def text_to_speech(text: str, voice: str) -> None:
    communicate = edge_tts.Communicate(text,voice)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_path = tmp_file.name
        communicate.save(tmp_path)
    return tmp_path

#'en-GB-SoniaNeural'