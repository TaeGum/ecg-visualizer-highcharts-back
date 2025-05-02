# ecg-visualizer-highcharts-back

ECG(심전도) 데이터를 제공하는 FastAPI 기반 백엔드 프로젝트입니다.  
이 API는 프론트엔드에서 ECG 신호를 시각화하거나, 향후 어노테이션 및 AI 기반 분석 기능을 연동할 때 사용할 수 있습니다.

---

## Features

- 더미 ECG 데이터(Lead, 구간, 샘플레이트 등) 제공
- 확장 가능한 프로젝트 구조
- FastAPI 기반 RESTful API
- 자동 문서화(Swagger UI)

---

## Getting Started

### 1. 환경 준비

- Python 3.8 이상
- pip

### 2. 가상환경 생성 및 패키지 설치

```
python -m venv venv
venv\Scripts\activate # (Windows)
pip install -r requirements.txt
```


### 3. 서버 실행

```
uvicorn app.main:app --reload
```


### 4. API 테스트

- 브라우저에서 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 접속  
  (Swagger UI에서 직접 테스트 가능)
- 또는 아래와 같이 GET 요청:
```
GET /api/ecg?lead=II&start=0&end=10
```


---

## API 명세

### GET `/api/ecg`

**Query Parameters:**
- `lead` (string, optional): ECG 리드 (예: I, II, III 등)
- `start` (float, optional): 시작 시간 (초)
- `end` (float, optional): 종료 시간 (초)

**Response Example:**
```
{
"lead": "II",
"sample_rate": 250,
"data": [
{"time": 0.0, "amplitude": 0.12},
{"time": 0.004, "amplitude": 0.13},
...
]
}
```


---

## 프로젝트 구조

```
ecg-visualizer-highcharts-back/
├── app/
│ ├── init.py
│ ├── main.py
│ └── ecg_data.py
├── tests/
│ ├── init.py
│ └── test_main.py
├── requirements.txt
└── README.md
```


---

## License

MIT

