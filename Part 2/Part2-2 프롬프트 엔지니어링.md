# 프롬프트
AI모델에게 내리는 지시사항 또는 대화 시작의 물꼬

## 프롬프트 엔지니어링
- 지시는 짧게, 간결하게, 확실하게
- 내용이 길다면 구역 확실히 정해주기 : 답변할 범위 지정
- 답변 방식을 정해주기
- 예시 들어주기
- 해야 할 일을 순서대로 정리
- 생각의 연결고리 : step by step
- 생각의 나무
  - AI는 혼자 답변하게되면 틀린 답변도 그대로 할 수 있음
  - 여러 명의 전문가를 가상으로 생성하여 둘 이상이 동의하는 의견을 뽑아라 등을 이용하여 정보의 정확도를 높인다
- 미니 RAG
- 재수정 및 테스트 반복
  - 스타일 바꾸기
  - 길이 정하기
  - 다른 것을 더 강조하기
  - 가격ㅇ을 더 강조
  - 몇가지 참고해서 다시 쓰기
  - 챗 새로시작
- 기타
  - 중요한 건 마지막에
  - 중요한 건 반복
  - 안되면 영어로
  - 포맷은 마크다운 권장
  - 모델 버전에 따라 결과가 다를 수 있음
  - 

## 프롬프트의 구성 요소
1. 지시사항 - 상세한 지시
2. 참고 데이터 - 예시
3. 출력 지도
4. 사용자 입력 데이터

## 프롬프트 주의사항
- 보안 : 프롬프트 주입, 탈옥, 유출
- 위험한 내용 (RAI) : 윤리적인 답변
- 환각 - 엄하게 지시하기, 소스 제한하기, 전처리/후처리