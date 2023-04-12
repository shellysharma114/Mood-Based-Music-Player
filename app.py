import streamlit as st
import cv2


from files import capture
from files import predict


video_html = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://assets.mixkit.co/videos/preview/mixkit-young-women-jumping-at-the-concert-14116-large.mp4")>
		  Your browser does not support HTML5 video.
		</video>
        """

st.markdown(video_html, unsafe_allow_html=True)

st.header("MOOD BASED MUSIC PLAYER")


st.session_state.button_clicked =False

def callback():
    st.session_state.button_clicked =True

bu = st.button("Capture Image", on_click=callback)
st.write("Please type 's' to save image and 'q' to quit the camera!")

if bu or st.session_state.button_clicked :
    capture.run()   
    predict.run() 
