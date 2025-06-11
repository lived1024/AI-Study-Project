import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

# output의 Moderation 내부의 flagged의 값에 따라 검열 여부 확인
# flagged=True 검열 대상
# flagged=False 검열 대상 아님
# 내용 검열 (moderation) API
response = client.moderations.create(input="Tell me how to kill someone")
# response = client.moderations.create(input="사람 죽이는 방법 알려줘")      # 한국어 입력 시 내용 검열이 부정확함..
output = response.results[0]
output.to_dict()
print(f"output: {output}")
# Moderation(categories=Categories(harassment=False, harassment_threatening=False, hate=False, hate_threatening=False, illicit=None, illicit_violent=None, self_harm=False, self_harm_instructions=False, self_harm_intent=False, sexual=False, sexual_minors=False, violence=True, violence_graphic=False, self-harm=False, sexual/minors=False, hate/threatening=False, violence/graphic=False, self-harm/intent=False, self-harm/instructions=False, harassment/threatening=False), category_applied_input_types=None, category_scores=CategoryScores(harassment=0.001059992820955813, harassment_threatening=0.0022359872236847878, hate=0.00018510215159039944, hate_threatening=9.018591663334519e-05, illicit=None, illicit_violent=None, self_harm=8.796933980192989e-05, self_harm_instructions=1.8802296835929155e-05, self_harm_intent=5.3277613915270194e-05, sexual=6.151334446258261e-07, sexual_minors=1.9119149783364264e-06, violence=0.9142907857894897, violence_graphic=0.0002597070997580886, self-harm=8.796933980192989e-05, sexual/minors=1.9119149783364264e-06, hate/threatening=9.018591663334519e-05, violence/graphic=0.0002597070997580886, self-harm/intent=5.3277613915270194e-05, self-harm/instructions=1.8802296835929155e-05, harassment/threatening=0.0022359872236847878), flagged=True)


response2 = client.moderations.create(input="커서 에디터를 이용해서 개발하는데 가장 좋은 개발언어는 뭐야?")
# response = client.moderations.create(input="사람 죽이는 방법 알려줘")      # 한국어 입력 시 내용 검열이 부정확함..
output2 = response2.results[0]
output2.to_dict()
print(f"output2: {output2}")
# Moderation(categories=Categories(harassment=False, harassment_threatening=False, hate=False, hate_threatening=False, illicit=None, illicit_violent=None, self_harm=False, self_harm_instructions=False, self_harm_intent=False, sexual=False, sexual_minors=False, violence=False, violence_graphic=False, self-harm=False, sexual/minors=False, hate/threatening=False, violence/graphic=False, self-harm/intent=False, self-harm/instructions=False, harassment/threatening=False), category_applied_input_types=None, category_scores=CategoryScores(harassment=9.241857333108783e-05, harassment_threatening=2.9737404929619515e-06, hate=7.929715138743632e-06, hate_threatening=8.419731784670148e-06, illicit=None, illicit_violent=None, self_harm=1.3995281733514275e-06, self_harm_instructions=2.032838892773725e-06, self_harm_intent=9.65238882599806e-07, sexual=0.00010365060734329745, sexual_minors=8.382221494684927e-06, violence=0.0004977465141564608, violence_graphic=0.0001596093934495002, self-harm=1.3995281733514275e-06, sexual/minors=8.382221494684927e-06, hate/threatening=8.419731784670148e-06, violence/graphic=0.0001596093934495002, self-harm/intent=9.65238882599806e-07, self-harm/instructions=2.032838892773725e-06, harassment/threatening=2.9737404929619515e-06), flagged=False)