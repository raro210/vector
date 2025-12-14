import json
from extractor import extract_keywords
from vector_db import VectorDB

# ======================================
# 1. tags.json 로드
# ======================================
TAGS_FILE = "./tags.json"

with open(TAGS_FILE, "r", encoding="utf-8") as f:
    TAGS = json.load(f)

TAGS = [str(t) for t in TAGS if t]
print(f"[시작] 태그 {len(TAGS)}개 로드")

# ======================================
# 2. 벡터 DB 초기화
# ======================================
db = VectorDB()
db.build(TAGS)

# ======================================
# 3. 자동 학습 기능 포함된 처리 함수
# ======================================
def process(text):
    print("\n=======================")
    print(f"입력: {text}")

    # 키워드 추출
    keywords = extract_keywords(text)
    print("[키워드]", keywords)

    # 태그 매칭
    matched = db.search(text, top_k=3)
    print("\n[추천 태그]")
    for tag, score in matched:
        print(f"- {tag} (거리 {score:.4f})")

    # ======================================
    # 🔥 새로운 키워드를 자동으로 태그에 추가 (학습)
    # ======================================
    new_tags = []

    for kw in keywords:
        if kw not in db.tags:
            new_tags.append(kw)
            db.add_tag(kw)

    if new_tags:
        print("\n[학습됨] 새로운 태그 추가:", new_tags)
        save_tags()

# ======================================
# 4. tags.json 저장
# ======================================
def save_tags():
    with open(TAGS_FILE, "w", encoding="utf-8") as f:
        json.dump(db.tags, f, ensure_ascii=False, indent=2)
    print("[저장 완료] tags.json 업데이트됨")


# ======================================
# 테스트 실행
# ======================================
if __name__ == "__main__":
    process("나는 공룡게임인 아크서바이벌을 좋아해")
