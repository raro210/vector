import numpy as np
from embedder import embed

class VectorDB:
    def __init__(self):
        self.tags = []      # 태그 문자열
        self.vectors = []   # 리스트로 저장해야 append 가능

    def build(self, tags):
        print(f"[시작] 태그 {len(tags)}개 로드")
        self.tags = tags
        self.vectors = embed(tags)  # <-- numpy array로 반환됨! (중요)
        print(f"[VectorDB] 벡터 {len(self.vectors)}개 생성 완료")

    def cosine_distance(self, a, b):
        return 1 - np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b) + 1e-10)

    def search(self, text, top_k=5):
        query_vec = embed([text])[0]

        result = []
        for i in range(len(self.tags)):
            dist = self.cosine_distance(query_vec, self.vectors[i])
            result.append((self.tags[i], dist))

        result.sort(key=lambda x: x[1])
        return result[:top_k]

    def add_tag(self, tag):
        """
        새로운 태그 학습 추가
        """
        self.tags.append(tag)
        
        vec = embed([tag])[0]

        # 원래 self.vectors는 numpy 배열 → 리스트 변환 필요
        self.vectors = np.vstack([self.vectors, vec])
