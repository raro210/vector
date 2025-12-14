# Tag Recommender (FAISS + SentenceTransformers, OpenAI 없이)

## 요구사항
- Python 3.8+ (권장 3.10/3.12)
- WSL (Windows), macOS, Linux 모두 동작
- (가능하면) faiss-cpu 설치 권장. 설치 불가능 시 numpy fallback으로 동작

## 설치
1. 가상환경 생성 (권장)
   python3 -m venv venv
   source venv/bin/activate

2. 의존성 설치
   pip install -r requirements.txt

   만약 faiss-cpu 설치에서 문제 발생하면 다음과 같이 해보세요:
   - pip install sentence-transformers numpy scikit-learn
   (이 경우 코드가 numpy fallback 모드로 동작합니다.)

## 실행
1. (선택) data/extra_tags.txt에 추가 태그를 넣을 수 있음 (한 줄에 하나)
2. python main.py
3. 프롬프트에 자기소개를 입력하면 추천 태그와 점수가 출력됩니다.

## 예시 입력
- 라면을 좋아하는 착한 재능대학교 학생입니다.
- 새로운 기술을 배우는 것을 좋아하고 팀에서 일하는 것을 즐깁니다.

## 비고
- 모델: all-MiniLM-L6-v2 (가볍고 무료)
- FAISS가 설치되어 있으면 FAISS 인덱스를 사용하여 빠르게 유사도 검색을 수행합니다.
- konlpy/kiwipiepy/Java 같은 무거운 한글 형태소분석기는 사용하지 않도록 설계했습니다.
