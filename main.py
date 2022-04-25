from fileinput import filename
from imp import reload
import shutil
from typing import List
from fastapi import FastAPI,UploadFile,File,Request
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static")

path="static/media/"

templates = Jinja2Templates(directory="templates")


@app.get("/upload/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload/")
async def Upload(request: Request,files: List[UploadFile] = File(...)):
    for file in files:
        with open(path+file.filename,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
    im = Image.open(path+file.filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(path+'file.png') 
    filename = "/"+path+"file.png"  
    return templates.TemplateResponse('index.html',{"request": request,"filename":filename})


if __name__=='__main__':
    uvicorn.run("main:app",reload=True)