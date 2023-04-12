def run():
    import cv2
    import streamlit as st
    import webbrowser
    # from streamlit_webrtc import VideoProcessorBase, webrtc_streamer
    import numpy as np
    from streamlit_player import st_player

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    emotion =" "
    #iniciate id counter
    id = 0

    # Emotions related to ids: example ==> Anger: id=0,  etc
    names = ['Angry', 'Happy', 'Sad' ] 

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # ret, img =cam.read()
    img = cv2.imread("saved_img.jpg")
    # img = cv2.flip(img, -1) # Flip vertically
    if(img is not None):
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )

        
        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
            id = names[id]
            emotion = str(id)
            print(emotion)
            print(confidence)

    st.subheader("Here presenting a " + emotion + " playlist for you")
    if(emotion == 'Angry'):
        # Embed a youtube video
        st_player("https://www.youtube.com/playlist?list=PLFuSiQ0mwHUaC_wfLOPqnlcJJtvaIDfrB")
    elif(emotion == 'Happy'):
        # Embed a youtube video
        st_player("https://www.youtube.com/watch?v=oSpMspvMkSQ")
    elif(emotion =='Sad'):
        # Embed a youtube video
        st_player("https://www.youtube.com/watch?v=lTKeVdbiLjA")
    else:
        st.write("There is some error. Try Again!")

    print("\n [INFO] Done detecting")
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()