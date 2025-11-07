from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def msg():
    print("This server is running god dammit please work hard now!")

