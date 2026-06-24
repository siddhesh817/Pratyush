from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(
    title="Pratyush Retail Portal",
    description="FastAPI backend serving a unified digital storefront"
)

@app.get("/", response_class=HTMLResponse)
async def serve_storefront():
    # Reads the merged HTML file and serves it directly to the browser
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Error: index.html not found.</h1>", status_code=404)