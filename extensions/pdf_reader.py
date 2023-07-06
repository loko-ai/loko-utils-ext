from loko_extensions.model.components import Component, Input

pdf_reader_doc = '''
### Description

This component helps you reading textual content from a Machine Readable pdf.

The two **input** pins allow to extract the content both from a **url** and **file**, which can be read with a File Reader block. 

### How to use it

In case your file is available online and you don't want to download it, you can directly pass the url address as a string directly linking the flow to the *"url"* input pin of the *PDF Reader component*. For example, you may use a Trigger component, with *"String"* as *Type*, typing or pasting the url of interest in the *"Value"* field and then link it to the right input pin of the *PDF Reader*.

Otherwise, if the file you need to extract the content from is directly available on your computer, then you can link for instance a File Reader block, with the *"Read content"* field untoggled, to the *"file"* pin input. 

'''



pdf_reader_comp = Component("PDF Reader", inputs=[Input("file", service="pdf/text"), Input("url", service="pdf/url")], icon="RiFileList3Fill", description=pdf_reader_doc)