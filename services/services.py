import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger
from loko_extensions.business.decorator_fastapi import ExtractValueArgsFastAPI

from business.pdf_converter import pdf_to_image
from config.AppConfig import PORT

app = FastAPI()


@app.post('/convert_pdf', response_class=JSONResponse)
@ExtractValueArgsFastAPI(file=True)
def convert_pdf(file, args):
    directory = args.get("directory", None)
    logger.debug(directory)
    if not directory:
        msg = "Saving directory not specified! You have to specify the final directory of the image."
        raise HTTPException(status_code=400, detail=msg)
    pdf_to_image(file=file, directory=directory.get("path"))
    return JSONResponse("File correctly saved")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
