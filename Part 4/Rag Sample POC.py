# Proof of Concept
# ! pip install --quiet git+https://github.com/openai/whisper.git
# ! pip install --quiet sounddevice wavio
# ! pip install --quiet ipywebrtc notebook
# !apt install --quiet ffmpeg
# !apt-get install --quiet libportaudio2
# !pip install --quiet openai

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

# ipywebrtc에서 필요한 클래스들 import
from ipywebrtc import CameraStream, AudioRecorder

camera = CameraStream(constraints={'audio': True,'video':False})
recorder = AudioRecorder(stream=camera)
recorder


# 에디터에서는 녹음기 작동 불가 이슈
# Colab에서 작업 이어감
# https://colab.research.google.com/drive/19v_e_9IatHZEIZhksa5_Yvy9gXwvdpK7?usp=sharing