import io
import os

from loguru import logger
from loko_client.business.fs_client import FSClient
from pdf2image import convert_from_path, convert_from_bytes


GATEWAY = os.environ.get("GATEWAY", None) + "/routes"
# gw = 'http://gateway:8080/routes/'
logger.debug(f"gatweay path: {GATEWAY}")
fsclient = FSClient(gateway=GATEWAY)

def pdf_to_image(file, directory):
    fname = "".join(file.filename.split(".")[:-1])
    logger.debug(fname)
    logger.debug(directory)
    images = convert_from_bytes(file.file.read())
    for i in range(len(images)):
        # Save pages as images in the pdf
        buffer = io.BytesIO()
        images[i].save(buffer, 'png')
        save_msg = fsclient.save(directory+"/"+fname+".png", buffer.getvalue())
        # images[i].save('pageIIIIIIIII' + str(i) + '.jpg', 'JPEG')
        logger.debug(f"save msg: {save_msg}")
