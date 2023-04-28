import pytesseract

def cong():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
    config = ('-l kor+eng --oem 3 --psm 11')
    text = pytesseract.image_to_string(src_filtering, cotenfig=config)
    return text