import io
import os

from loguru import logger
from loko_client.business.fs_client import FSClient
from pdf2image import convert_from_path, convert_from_bytes

GATEWAY = os.environ.get("GATEWAY", None) + "/routes"
# gw = 'http://gateway:8080/routes/'
logger.debug(f"gatweay path: {GATEWAY}")
fsclient = FSClient(gateway=GATEWAY)


def pdf_to_image(file, directory, saving_ext):
    logger.debug(f"saving ext {saving_ext}")
    fname = "".join(file.filename.split(".")[:-1])
    logger.debug(fname)
    logger.debug(directory)
    images = convert_from_bytes(file.file.read())
    if len(images) == 0:
        raise Exception(f"ERROR!!! The file {fname} seems to be empty...")
    for i in range(len(images)):
        # Save pages as images in the pdf
        buffer = io.BytesIO()
        images[i].save(buffer, saving_ext.strip("."))
        page_name = fname + "_" + str(i + 1) + saving_ext
        logger.debug(f"pagename {page_name}")
        save_msg = fsclient.save(directory + "/" + page_name, buffer.getvalue())
        # images[i].save('pageIIIIIIIII' + str(i) + '.jpg', 'JPEG')
        logger.debug(f"save msg response: {save_msg}")
