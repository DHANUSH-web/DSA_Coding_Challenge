import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    hand_id = results.multi_hand_landmarks

    if hand_id:
        for handLms in hand_id:
            '''
            for iD, lm in enumerate(handLms.landmark):
                print(f"Id: {iD}\n{lm}")
            '''
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    c = int(time.strftime("%H"))

    if c > 12:
        c -= 12

    fps = f"Frame Rate: {int(fps)} FPS"
    d = "Date: " + time.strftime("%d/%m/%Y")
    t = "Time: " + time.strftime(f"{c} : %M : %S %p")

    cv2.putText(img, fps, (2, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 25), 1)
    cv2.putText(img, t, (2, 40), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 25), 1)
    cv2.putText(img, d, (2, 60), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 25), 1)

    # image show
    cv2.imshow("Hand Track", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
