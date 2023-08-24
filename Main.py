import subprocess
import customtkinter
from tkinter.filedialog import askopenfile
import os
import pyautogui

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("512x512")
app.title("CaptionCraft")

#the file we want to extract the subtitles from
file = ""

#Get the subtitles from the video file
def extract_subtitles()-> str:
    try:
        command = "ffmpeg -i " + file + " subs.srt"
        subprocess.call(command, shell=True)

        with open("subs.srt", "r") as f:
            lines = f.read()
            return lines
    
    except subprocess.CalledProcessError as e:
        print("Error: " + e.output)
        return None
    

def openFileButton():
    print("Open file button pressed")
    file = customtkinter.filedialog.askopenfile(mode='rb',filetypes=[('Mkv Files','.mkv')],title='Choose a file')
    filePath = os.path.abspath(file.name)
    titleLabel.configure(text=filePath)
    
def main():
    inputFile = ""
    extractedSubs = extract_subtitles(inputFile)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


#Top label
titleLabel = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
titleLabel.configure(text="CaptionCraft", font=("Arial", 20))
titleLabel.pack(pady=10, padx=10)

#Instructions label
instructionsLabel = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER)
titleLabel.configure(text="Select a folder with your MKV file to rename...", font=("Arial", 12))

#Start button
openFileButton = customtkinter.CTkButton(master=frame_1, command=openFileButton, text="Open File")
openFileButton.pack(pady=10, padx=10)

#Open file button
extract_subtitlesButton = customtkinter.CTkButton(master=frame_1, command=extract_subtitles, text="Open File")
extract_subtitlesButton.pack(pady=10, padx=10)




app.mainloop()