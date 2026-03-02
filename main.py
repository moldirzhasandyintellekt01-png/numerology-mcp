from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumerologyRequest(BaseModel):
    birth_date: str

def calculate_life_path(date: str):
    digits = [int(d) for d in date if d.isdigit()]
    total = sum(digits)
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

@app.post("/mcp")
def numerology_tool(data: NumerologyRequest):
    life_path = calculate_life_path(data.birth_date)

    return {
        "life_path_number": life_path,
        "message": f"Life Path {life_path} энергиясы белсенді"
    }
