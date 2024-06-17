import streamlit as st
from pytube import YouTube
import os

def download_youtube_video(url, download_location, folder_path=None):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    if download_location == "Mobile":
        video.download(output_path="/storage/emulated/0/Download")
        return f"Video downloaded: {yt.title}"
    elif download_location == "Computer":
        if folder_path:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            video_path = os.path.join(folder_path, f"{yt.title}.mp4")
            video.download(output_path=folder_path)
            return f"Video downloaded: {yt.title}"
        else:
            return "Please enter a download path."
    else:
        return "Please select a download location."

st.set_page_config(page_title="YouTube Video Downloader")

st.title("YouTube Video Downloader 📽️")
st.subheader("Paste the YouTube video link and select the download location")

video_url = st.text_input("Enter the YouTube video URL:")
download_location = st.selectbox("Select the download location:", ["Mobile", "Computer"])


if download_location == "Computer":
    folder_path = st.text_input('Input folder path')
# folder_path = st.text_input('Input folder path')


if st.button("Download Video"):
    try:
        if download_location == "Computer":
            message = download_youtube_video(video_url, download_location,folder_path)
            st.success(message)
        elif download_location == "Mobile":
            message = download_youtube_video(video_url, download_location)
            st.success(message)
        else:
            st.error("Please select a download location.")
    except Exception as e:
        st.error(f"Error downloading the video: {e}")