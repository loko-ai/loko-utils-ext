from loko_extensions.model.components import Component, Input, Arg, Output, save_extensions

directory = Arg(type="directories", name="directory", label="Saving directory")
args = [directory]
input_list = [Input(id="convert_pdf", label="convert pdf", to= "convert_pdf", service="convert_pdf")]
output_list = [Output(id="convert_pdf", label="convert pdf")]
pdf2image_component = Component(name="PDF2Image", inputs=input_list, outputs=output_list, args=args, icon="RiArrowGoForwardLine")
