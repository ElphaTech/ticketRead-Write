import cv2
# initalize the cam and detector
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        for i in range(len(bbox)):
            # draw all lines
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=100)
        if data:
            print("[+] QR Code detected, data:", data)
    # display the result
    cv2.imshow("img", img)    
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()