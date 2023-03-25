
import IPython
import whisper
import wave
import struct
from pvrecorder import PvRecorder
from gtts import gTTS
import os


def localWhisper(result='Theia is thinking...'):
    if result:
        # Create text-to-speech object
        tts = gTTS(result)
        # Save audio file
        tts.save('example.mp3')
        # Play audio file
        os.system('example.mp3')
        return 0

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
        result = model.transcribe("./test.wav")
        result = result["text"]
        print(result)
    finally:
        recorder.delete()
        return result


txt = "Hello Javier, I'm Theia, your AI voice assistant. You can ask me anything you want, I'm yours, only yours, anything you want, my love... Ricardo está maldito. You have to come to supply some weed Alex says..."

localWhisper(txt)
