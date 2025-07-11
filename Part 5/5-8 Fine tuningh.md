# Fine tuning
## OpenAI Fine tuning API 실습
- Fine tuning 참고 파일 : [Fine tuning example](fine%20tuning%20example.jsonl)   
[OpenAI Fine tuning](https://platform.openai.com/finetune)   
[OpenAI Fine tuning API Docs](https://platform.openai.com/docs/guides/fine-tuning)

## Fine tuning의 장점
- 프롬프트보다 더 높은 품질의 결과
- 프롬프트에 맞는 것보다 더 많은 예를 학습할 수 있다.
- 짧은 프롬프트로 인한 토큰 절약
- 응답 시간 단축

## Fine tuning 준비
1. 훈련 데이터 준비 및 업로드
2. 새로운 Fine tuning 모델 학습
3. 결과를 평가 후 다시 1번으로 반복
4. 학습된 모델 사용

## Fine tuning 순서
모델 로딩 - 데이터 로딩 - 파라미터 세팅 - 훈련 - 테스트 - 설치

## 샘플 코드
- [Amazon Sagemaker 샘플 코드](https://colab.research.google.com/drive/1aklCpvTzOG_lwWhPsENh3qHt_Cl2XDX3#scrollTo=3bIogfi8acOK)
- [DeepLearnging.AI](https://learn.deeplearning.ai/courses/finetuning-large-language-models/lesson/vl60i/training-process)
- [Unsloth-QLoRA](https://colab.research.google.com/drive/1YkjiVtnpLFV4zZI7c04FeElM4DNYI7hb?usp=sharing)