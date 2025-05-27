import os
import openai

def load_openai_api_key():
    """
    OPENAI_API_KEY 파일에서 API 키를 읽어와서 환경변수에 설정하고 openai 클라이언트를 반환합니다.
    
    Returns:
        openai.OpenAI: 설정된 OpenAI 클라이언트
    """
    # 현재 파일의 디렉토리로 이동
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    # 같은 디렉토리의 OPENAI_API_KEY.txt 파일에서 API 키 읽기
    with open('OPENAI_API_KEY.txt', 'r') as file:
        api_key = file.read().strip()
    
    # 환경변수에 설정
    os.environ["OPENAI_API_KEY"] = api_key
    
    # openai.api_key도 설정 (하위 호환성을 위해)
    openai.api_key = api_key
    
    # OpenAI 클라이언트 생성 및 반환
    return openai.OpenAI()

def get_openai_api_key():
    """
    환경변수에서 OpenAI API 키를 가져옵니다.
    
    Returns:
        str: OpenAI API 키
    """
    return os.getenv("OPENAI_API_KEY") 