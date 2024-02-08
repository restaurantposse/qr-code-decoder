import cv2
qr_detector = cv2.QRCodeDetector()

try:
    result, _, _ = qr_detector.detectAndDecode(cv2.imread('img/img.png'))
    print(result)
except cv2.error as err:
    print(f"Provided file probably does not exist. {err}")
