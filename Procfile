web: gunicorn app:app
# import os
# os.environ["CUDA_VISIBLE_DEVICES"]= "-1"
# import cv2
# from deepface import DeepFace

# face_classifier = cv2.CascadeClassifier()
# face_classifier.load(cv2.samples.findFile("haarcascade_frontalface_default.xml"))

# cap = cv2.VideoCapture(0)

# while True:
    
#     ret, frame = cap.read()
#     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(frame_gray)
    
#     response = DeepFace.analyze(frame, actions=("emotion",), enforce_detection=False)
#     for face in faces:
#         x,y,w,h = face
        
#         cv2.rectangle(frame, (x+10,y+10), (x+w,y+h), color= (238,130,238), thickness=4)
#         cv2.putText(frame, response["dominant_emotion"].upper(), org=(x,y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
#             fontScale=1.2, color=(255,204,153),thickness=4)
#         cv2.imshow("", frame)
#         if(cv2.waitKey(30)==27):
#             break
# cap.release()
# cv2.destroyAllWindows()