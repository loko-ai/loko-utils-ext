from loko_extensions.model.components import save_extensions

from extensions.pdf2image_comp import pdf2image_component
from extensions.pdf_reader import pdf_reader_comp

if __name__ == '__main__':
    save_extensions([pdf2image_component, pdf_reader_comp])