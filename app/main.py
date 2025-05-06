from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

# 허용할 origin(출처) 목록
origins = [
    "http://localhost:3000",  # Next.js 개발 서버
    "https://ecg-visualizer-highcharts-front.vercel.app",  # 프로덕션 환경 도메인 (필요시 추가)
]

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 허용할 출처
    allow_credentials=True,           # 쿠키 등 자격 증명 허용 여부
    allow_methods=["*"],              # 모든 HTTP 메서드 허용
    allow_headers=["*"],              # 모든 헤더 허용
)

@app.get("/api/ecg")
async def get_ecg(lead: str = "II", start: float = 0, end: float = 10):
    sample_rate = 250
    duration = end - start
    t = np.linspace(start, end, int(sample_rate * duration))
    signal = 0.6 * np.sin(2 * np.pi * 1.7 * t) + 0.1 * np.random.normal(size=len(t))
    data = [{"time": round(float(time), 3), "amplitude": round(float(amp), 3)} for time, amp in zip(t, signal)]
    return {"lead": lead, "sample_rate": sample_rate, "data": data}
