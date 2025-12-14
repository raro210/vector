# server.py
from fastapi import FastAPI
from pydantic import BaseModel
# 네가 만든 키워드 추출 함수 가져오기 (파일명이 extractor.py라고 가정)
from extractor import extract_keywords 

app = FastAPI()

# Node.js에서 보낼 데이터 형식 정의
class UserBio(BaseModel):
    text: str

@app.post("/analyze")
def analyze_bio(item: UserBio):
    print(f"요청받은 내용: {item.text}")
    
    # 1. 여기서 네가 만든 AI 기능 돌리기
    keywords = extract_keywords(item.text) # 기존 함수 사용
    
    # 2. 결과 돌려주기
    return {"result_tags": keywords}

# 실행되면 모델은 메모리에 계속 떠있어서 속도가 엄청 빨라짐!