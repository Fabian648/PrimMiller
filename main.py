from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import random

app = FastAPI(title="Primzahl-API", description="Prüft, ob eine Zahl eine Primzahl ist.", version="1.0")

def is_prime(n: int, k: int = 5) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Schreibe n-1 als 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

@app.get("/is_prime")
def check_prime(number: int = Query(..., gt=0, description="Die zu prüfende Zahl")):
    result = is_prime(number)
    return JSONResponse(content={"number": number, "is_prime": result})
