import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

# 음성 추출
audio_file = open("./김동률 - 다시 사랑한다 말할까.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print("Extract Done")
print(transcription.text)


# 음성 추출하여 번역
translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
)
print(translation.text)


# # 음성 생성
speech_file = "speech_output_translations.mp3"
with client.audio.speech.with_streaming_response.create(
  model="tts-1",
  voice="nova",
  # input=transcription.text    # 원본 음성
  input=translation.text        # 번역 음성
) as response:
    response.stream_to_file(speech_file)
print("Create Finished")

