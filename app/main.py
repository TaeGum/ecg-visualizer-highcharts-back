from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/api/ecg")
async def get_ecg(lead: str = "II", start: float = 0, end: float = 10):
    sample_rate = 250
    duration = end - start
    t = np.linspace(start, end, int(sample_rate * duration))
    signal = 0.6 * np.sin(2 * np.pi * 1.7 * t) + 0.1 * np.random.normal(size=len(t))
    data = [{"time": round(float(time), 3), "amplitude": round(float(amp), 3)} for time, amp in zip(t, signal)]
    return {"lead": lead, "sample_rate": sample_rate, "data": data}
