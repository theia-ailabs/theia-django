import whisper
import wave
import struct
from pvrecorder import PvRecorder
from gtts import gTTS
from src.apis.openai_api import davinci
import os


def localListener(file='result.mp3', result=''):
    if result:
        # Create text-to-speech object
        tts = gTTS(result)
        # Save audio file
        tts.save(file)
        # Play audio file
        os.system(file)
        return 0


def localWhisper():
    result = ''
    try:
        # load audio drivers
        for index, device in enumerate(PvRecorder.get_audio_devices()):
            print(f"[{index}] {device}")
        # init recorder driver
        recorder = PvRecorder(device_index=-1, frame_length=512)
        path = 'temp.wav'
        audio = []
        recorder.start()
        while True:
            frame = recorder.read()
            audio.extend(frame)
    except KeyboardInterrupt:
        recorder.stop()
        with wave.open(path, 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
        model = whisper.load_model("base")
        text = model.transcribe("./temp.wav")
        text = text["text"]
        print('\n', text)
        result = davinci(text)
        print('\n', result)
        localListener('temp.wav', result)
    finally:
        recorder.delete()
        return result


txt = "Hello world, I'm Theia, your AI voice assistant. You can ask me anything you want."

localWhisper()
