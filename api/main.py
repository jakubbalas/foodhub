from fastapi import FastAPI


app = FastAPI()


@app.get("/ingredients/{ingredient_id}")
def get_ingredients(ingredient_id: int | None = None) -> list[dict]:
    return [
        {
            "id": ingredient_id,
            "name": "water",
        }
    ]
