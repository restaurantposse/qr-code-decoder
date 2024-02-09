import cv2
from pyzbar.pyzbar import decode


def qr_barcode_detect(path):
    qr_detector = cv2.QRCodeDetector()
    img = cv2.imread(path)
    try:
        result, _, _ = qr_detector.detectAndDecode(img)
        if result == '':
            barcode_scanner = decode(img)
            for barcode in barcode_scanner:
                if barcode.data is not None:
                    print("BARCODE")
                    return barcode.data
            print("Image doesn't contain any QR code or barcode.")
            return None
        else:
            return result
    except cv2.error as err:
        print(f"Provided file probably does not exist. {err}")


if __name__ == "__main__":
    res = qr_barcode_detect('img/img_1.png')
    print(res)
