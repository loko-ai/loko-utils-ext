import shutil
import urllib
from io import BytesIO

import fitz as fitz
import requests
import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger
from loko_extensions.business.decorator_fastapi import ExtractValueArgsFastAPI

from business.pdf_converter import pdf_to_image
from config.AppConfig import PORT

app = FastAPI()


@app.exception_handler(Exception)
async def handle_exception(request, exc):
    # Log the exception
    logger.error(str(exc))

    # Propagate the exception as a JSON response
    response_data = {"detail": str(exc)}
    response_json = jsonable_encoder(response_data)
    return JSONResponse(status_code=500, content=response_json)


@app.post('/convert_pdf', response_class=JSONResponse)
@ExtractValueArgsFastAPI(file=True)
def convert_pdf(file, args):
    logger.debug(f"args:: {args}")
    directory = args.get("directory", None)
    saving_ext = args.get("saving_ext", ".png")
    if not directory:
        msg = "Saving directory not specified! You have to specify the final directory of the image."
        raise HTTPException(status_code=400, detail=msg)
    pdf_to_image(file=file, directory=directory.get("path"), saving_ext=saving_ext)
    return JSONResponse("File correctly saved")


@app.post("/pdf/text")
@ExtractValueArgsFastAPI(file=True)
def pdf_text(file, args):
    buffer = BytesIO()
    with buffer:
        shutil.copyfileobj(file.file, buffer)
        # file.save(buff)
        n = buffer.tell()
        buffer.seek(0)
        doc = fitz.open("pdf", buffer)
        text = []
        for page in doc:
            text.append(page.get_text())
    return JSONResponse(" ".join(text))


@app.post("/pdf/url")
@ExtractValueArgsFastAPI()
def pdf_url(value, args):
    value = urllib.parse.unquote(value)
    raw = requests.get(value).content
    buff = BytesIO()
    buff.write(raw)
    buff.seek(0)
    doc = fitz.open("pdf", buff)
    text = []
    for page in doc:
        text.append(page.get_text().strip())
    return JSONResponse(" ".join(text))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
