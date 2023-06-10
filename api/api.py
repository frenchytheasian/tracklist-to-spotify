from fastapi import FastAPI

app = FastAPI()


@app.get("/playlist/")
async def get_playlist(link: str):
    return link