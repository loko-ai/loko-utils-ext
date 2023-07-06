from loko_extensions.model.components import Component, Input, Arg, Output, save_extensions, Select

pdf2image_doc = '''
### Description

The **PDF2Image** component allows to convert a pdf file into an image file. The converted file will have the same filename, to which will be add the relative page number of the pdf converted, and the file extensions of the image chosen.
For instance, if your file it's called "file.pdf" and you contains only 1 page, then the new file, supposing we are saving it as ".png", will be saved as "file_1.png". 

### Settings

In the *"Image extension"* field select the extension that you want to us for the image, the default value is *".png"*.
In the *"Saving directory"* field select the directory in which you want to save the resulting file.

'''

directory = Arg(type="directories", name="directory", label="Saving directory")
saving_ext = Select(name="saving_ext", label="Image extension", options=[".png", ".jpg"], value=".png")
args = [saving_ext, directory]
input_list = [Input(id="convert_pdf", label="convert pdf", to= "convert_pdf", service="convert_pdf")]
output_list = [Output(id="convert_pdf", label="convert pdf")]
pdf2image_component = Component(name="PDF2Image", inputs=input_list, outputs=output_list, args=args, icon="RiArrowGoForwardLine", description=pdf2image_doc)
