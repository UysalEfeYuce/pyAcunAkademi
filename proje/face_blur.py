
import cv2

print("Program baslatiliyor.")

try:
    print("Yuz algilama yukleniyor.")
    yuz_algila = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    if yuz_algila.empty():
        print("HATA: Yuz algilama dosyasi yuklenemedi.")
        input("Devam etmek istiyorsaniz Enter'a basin.")
        exit()

    print("Kamera aciliyor...")
    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("HATA: Kamera acilamadi")
        input("Devam etmek istiyorsaniz Enter'a basin.")
        exit()

    print("Kamera acildi. 'Q' tusuna basarak cikabilirsiniz.")

    while True:
        ret, frame = kamera.read()
        if not ret:
            print("Kameradan goruntu alinamiyor")
            break

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        yuzler = yuz_algila.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(150, 150), maxSize=(300, 300))

        for (x, y, w, h) in yuzler:
            face_roi = frame[y:y+h, x:x+w]
            blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
            frame[y:y+h, x:x+w] = blurred_face

        cv2.imshow("Yuz Blur", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"HATA olustu: {e}")
    input("Devam etmek istiyorsaniz Enter'a basin.")

finally:
    print("Program kapatiliyor.")
    try:
        kamera.release()
        cv2.destroyAllWindows()
    except:
        pass
    input("Cikis icin Enter'a basin.")

