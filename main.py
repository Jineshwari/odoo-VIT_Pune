from fastapi import FastAPI, File, UploadFile
import pytesseract
import cv2
import numpy as np
import re
import easyocr

# 🔴 SET YOUR PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AASHANA\tesseract.exe"

app = FastAPI()

# Load EasyOCR once
reader = easyocr.Reader(['en'])


@app.get("/")
def home():
    return {"message": "OCR Receipt API Ready 🚀"}


# =========================
# 🧠 TEXT EXTRACTION
# =========================
def run_ocr(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 3)
    gray = cv2.convertScaleAbs(gray, alpha=2, beta=20)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    config = r'--oem 3 --psm 4'
    text = pytesseract.image_to_string(thresh, config=config)

    # fallback
    if len(text.strip()) < 30:
        result = reader.readtext(img)
        text = " ".join([r[1] for r in result])

    # clean noise
    text = text.replace('[', '').replace(']', '')

    return text


# =========================
# 🏪 VENDOR EXTRACTION
# =========================
def extract_vendor(text):
    lines = text.split("\n")

    for line in lines:
        clean = line.strip()

        # remove symbols/numbers
        clean = re.sub(r'[^A-Z\s]', '', clean)

        if len(clean) > 5 and clean.isupper():
            words = clean.split()
            return " ".join(words[:3])  # max 3 words

    # fallback
    for line in lines[:3]:
        clean = line.strip()
        if len(clean) > 3:
            words = clean.split()
            return " ".join(words[:3])

    return "Unknown"


# =========================
# 🔍 DATA EXTRACTION
# =========================
def extract_data(text):
    # 💰 amounts
    amounts = re.findall(r'\d+[.,]\d{2}', text)
    amounts = [a.replace(',', '.') for a in amounts]

    float_amounts = []
    for a in amounts:
        try:
            float_amounts.append(float(a))
        except:
            continue

    # 🎯 total
    total_amount = 0
    total_match = re.search(r'total[^0-9]*(\d+[.,]\d{2})', text, re.IGNORECASE)

    if total_match:
        total_amount = float(total_match.group(1).replace(',', '.'))
    elif float_amounts:
        total_amount = max(float_amounts)

    # 📅 date
    dates = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text)

    # 🏪 vendor
    vendor = extract_vendor(text)

    return {
        "total_amount": total_amount,
        "all_amounts": amounts,
        "date": dates[0] if dates else None,
        "vendor": vendor
    }


# =========================
# 🌐 API
# =========================
@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    text = run_ocr(img)

    structured = extract_data(text)

    return {
        "raw_text": text,
        "structured_data": structured,
        "status": "success"
    }