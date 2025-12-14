from sentence_transformers import SentenceTransformer

# 안전하게 모델 로드
model = SentenceTransformer("jhgan/ko-sroberta-multitask")

def embed(sentences):
    """
    문장 리스트를 받아서 벡터로 변환
    """
    # 문자열만 남기기
    sentences = [str(s) for s in sentences if s]
    if not sentences:
        return []
    return model.encode(sentences, convert_to_numpy=True)

def embed_text(sentences):
    return embed(sentences)