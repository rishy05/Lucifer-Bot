import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd =r'PATH TO TESSERACT'
def txt(path):
    img= Image.open(path)
    text = tess.image_to_string ( img )
    return(text)

