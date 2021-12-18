#pip install opencv-python
#pip install mediapipe

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

  while cap.isOpened():

    test, image = cap.read()

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    height, width, _ = image.shape

    results = face_mesh.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_face_landmarks:
      for face_landmarks in results.  multi_face_landmarks:

        point9 = face_landmarks.landmark[9]
        pt9x = int(point9.x * width)
        pt9y = int(point9.y * height)
        cv2.circle(image,(pt9x,pt9y),5,(10,10,10), -1)

        point10 = face_landmarks.landmark[10]
        pt10x = int(point10.x * width)
        pt10y = int(point10.y * height)
        cv2.line(image, (pt9x, pt9y),(pt10x,pt10y), (0,0,0), 2, -1)

    cv2.imshow('Nama Cam', image)

    if cv2.waitKey(0) & 0xFF == ord('q'):
      break