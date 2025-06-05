# pip install ragas
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, faithfulness, context_recall, answer_correctness, context_precision

def ragas_evaluate(eval_sets):
  return evaluate(
    eval_sets,
    metrics=[
        context_precision,
        faithfulness,
        answer_relevancy,
        context_recall,
        answer_correctness
    ]
  )

# 답변할 수 있게 잘 뽑은 참고 자료 (컨텍스트)
busan_context_right = [
  "Busan is divided into 15 major administrative districts and a single county, together housing a population of approximately 3.6 million."
  "Busan (Korean: 부산, pronounced [pusan]), officially Busan Metropolitan City, is South Korea's second most populous city after Seoul, with a population of over 3.4 million inhabitants as of 2017.[4] Formerly romanized as Pusan (and Fuzan under Japanese rule)."
  "부산광역시(釜山廣域市, 영어: Busan Metropolitan City)는 한반도 남동부에 위치한 광역시이다. 대한민국의 제2의 도시이자 최대의 해양(항구) 도시이며, 부산항을 중심으로 해상 무역과 물류 산업이 발달하였다. 일본과는 대한해협을 사이에 두고 마주하고 있다. 시청 소재지는 연제구 연산동이며, 행정구역은 15구 1군이다."
]
# 컨텍스트
busan_context_wrong_1 = ["부산에는 호떡이 맛있다.", "부산에는 언덕이 많다."]
busan_context_wrong_2 = ["호떡이 맛있다.", "언덕이 많다."]


# # 세트 1 - 정답, 그리고 좋은 컨텍스트
# eval_set1 = {
# 	"question": ["대한민국에서 두번째로 큰 도시는 어디야?"],     # 질문
# 	"answer"  : ["대한민국에서 두번째로 큰 도시는 부산입니다."],  #  언어 모델이 내놓은 답
# 	"contexts": [busan_context_right],                         # 참고 자료
# 	"ground_truth": ["부산"]                                   # 정답
# }
# eval_sets1 = Dataset.from_dict(eval_set1)

# # {'context_precision': 0.0000, 'faithfulness': 0.0000, 'answer_relevancy': 0.9079, 'context_recall': 0.0000, 'answer_correctness': 0.9729}
# print(f"세트 1 정답 : {ragas_evaluate(eval_sets1)}")


# # 세트 2 - 오답, 그러나 좋은 컨텍스트.
# eval_set2 = {
# 	"question": ["대한민국에서 두번째로 큰 도시는 어디야?"],     # 질문
# 	"answer"  : ["부산은 한국에 있다."],                      #  언어 모델이 내놓은 답
# 	"contexts": [busan_context_right],                         # 참고 자료
# 	"ground_truth": ["부산"]                                   # 정답
# }
# eval_sets2 = Dataset.from_dict(eval_set2)

# # {'context_precision': 0.0000, 'faithfulness': 0.0000, 'answer_relevancy': 0.8117, 'context_recall': 1.0000, 'answer_correctness': 0.7295}
# print(f"세트 2 오답 : {ragas_evaluate(eval_sets2)}")


# # 세트 3 - 정답, 그러나 불량 컨텍스트
# eval_set3 = {
# 	"question": ["대한민국에서 두번째로 큰 도시는 어디야?"],     # 질문
# 	"answer"  : ["대한민국에서 두번째로 큰 도시는 부산입니다."],  #  언어 모델이 내놓은 답
# 	"contexts": [busan_context_wrong_1],                         # 참고 자료
# 	"ground_truth": ["부산"]                                   # 정답
# }
# eval_sets3 = Dataset.from_dict(eval_set3)

# # {'context_precision': 0.0000, 'faithfulness': 0.0000, 'answer_relevancy': 0.9369, 'context_recall': 1.0000, 'answer_correctness': 0.9729}
# print(f"세트 3 정답 : {ragas_evaluate(eval_sets3)}")


# 세트 4 - 정답, 그러나 불량 컨텍스트 (컨텍스트에 부산이라는 단어도 없음)
# eval_set4 = {
# 	"question": ["대한민국에서 두번째로 큰 도시는 어디야?"],     # 질문
# 	"answer"  : ["대한민국에서 두번째로 큰 도시는 부산입니다."],  #  언어 모델이 내놓은 답
# 	"contexts": [busan_context_wrong_2],                         # 참고 자료
# 	"ground_truth": ["부산"]                                   # 정답
# }
# eval_sets4 = Dataset.from_dict(eval_set4)

# # {'context_precision': 0.0000, 'faithfulness': 0.0000, 'answer_relevancy': 0.9079, 'context_recall': 0.0000, 'answer_correctness': 0.9729}
# print(f"세트 4 정답 : {ragas_evaluate(eval_sets4)}")


# # 세트 5 - 오답, 그러나 좋은 컨텍스트
# eval_set5 = {
# 	"question": ["대한민국에서 두번째로 큰 도시는 어디야?"],     # 질문
# 	"answer"  : ["대한민국에서 두번째로 큰 도시는 대구입니다."],  #  언어 모델이 내놓은 답
# 	"contexts": [busan_context_right],                         # 참고 자료
# 	"ground_truth": ["부산"]                                   # 정답
# }
# eval_sets5 = Dataset.from_dict(eval_set5)

# # {'context_precision': 1.0000, 'faithfulness': 0.0000, 'answer_relevancy': 0.9369, 'context_recall': 1.0000, 'answer_correctness': 0.2067}
# print(f"세트 5 정답 : {ragas_evaluate(eval_sets5)}")


# 세트 6 - 오답, 그러나 좋은 컨텍스트
eval_set6 = {
	"question": ["대한민국에서 두번째로 큰 도시는 어디야?"],     # 질문
	"answer"  : ["대한민국에서 두번째로 큰 도시는 대구입니다."],  #  언어 모델이 내놓은 답
	"contexts": [busan_context_right],                         # 참고 자료
	"ground_truth": ["부산은 호떡이 맛있다"]                                   # 정답
}
eval_sets6 = Dataset.from_dict(eval_set6)

# {'context_precision': 0.0000, 'faithfulness': 0.0000, 'answer_relevancy': 0.9079, 'context_recall': 0.0000, 'answer_correctness': 0.2018}
print(f"세트 6 정답 : {ragas_evaluate(eval_sets6)}")