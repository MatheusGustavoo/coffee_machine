from fastapi import FastAPI
from src.routes.produtos import produtos_router

app = FastAPI()

app.include_router(produtos_router)

def main():
    print("Hello from coffe-machine!")


if __name__ == "__main__":
    main()
