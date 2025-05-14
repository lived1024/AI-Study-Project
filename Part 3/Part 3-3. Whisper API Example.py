import openai
import os

# API_KEY.txt 파일에서 API 키 읽기
# API_KEY.txt 파일은 현재 작업 디렉토리에 있어야 합니다.
# 이 코드는 현재 작업 디렉토리로 이동하여 API_KEY.txt 파일을 읽습니다.
os.chdir(os.path.dirname(__file__))
with open('API_KEY.txt', 'r') as file:
    os.environ["OPENAI_API_KEY"] = file.read().strip()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

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


# 음성 생성
speech_file = "speech_output_translations.mp3"
with client.audio.speech.with_streaming_response.create(
  model="tts-1",
  voice="nova",
  # input=transcription.text    # 원본 음성
  input=translation.text        # 번역 음성
) as response:
    response.stream_to_file(speech_file)
print("Create Finished")

