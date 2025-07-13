# LoRA, Quantization

## Fine tuning의 두 가지 접근 방식
### Full Fine-tuning (전체 파인튜닝)
- 모델의 모든 파라미터를 새로운 데이터로 재학습
- 높은 성능을 얻을 수 있지만 많은 메모리와 계산 자원 필요
- 대규모 모델에서는 비용과 시간이 많이 소요

### PEFT (Parameter-Efficient Fine-Tuning)
- 모델의 일부 파라미터만 학습하여 효율성 극대화
- 원본 모델을 보존하면서 새로운 태스크에 적응
- 대표적 기법: LoRA, Adapter, Prompt Tuning 등


## 주요 용어
### PEFT (Parameter-Efficient Fine-Tuning)
- 전체 모델을 재학습하지 않고 일부 파라미터만 조정하는 효율적인 파인튜닝 기법
- 메모리 사용량과 학습 시간을 크게 절약

### LoRA (Low-Rank Adaptation)
- 기존 가중치는 고정하고 저랭크 행렬을 추가하여 학습하는 방법
- 원본 모델 유지하면서 새로운 태스크에 빠르게 적응 가능

### QLoRA (Quantized LoRA)
- LoRA에 양자화 기법을 결합하여 효율성을 극대화
- 메모리 사용량과 컴퓨팅 요구사항을 대폭 감소
- 일반 소비자용 하드웨어에서도 대규모 모델 미세조정 가능
- [QLoRA 가이드 문서](https://github.com/peremartra/Large-Language-Model-Notebooks-Course/blob/main/5-Fine%20Tuning/QLoRA_Tuning_PEFT.ipynb)

### Quantization (양자화)
- 모델의 가중치 정밀도를 낮춰 메모리 사용량과 연산 속도를 개선
- FP32 → FP16, INT8 등으로 변환하여 모델 크기 축소
- 성능 손실 최소화와 함께 저사양 하드웨어에서도 실행 가능