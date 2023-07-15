import tkinter
import customtkinter
from pytube import YouTube

def onProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercent.configure(text=per + '%')
    pPercent.update()

    # update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

def startDownload():
    try:
        urlLink = link.get()
        ytObject = YouTube(urlLink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()


        title.configure(text=ytObject.title, text_color="white")
        finishedLabel.configure(text="")
        video.download()
        finishedLabel.configure(text="Download complete")
    except:
        finishedLabel.configure(text="Error downloading the file.", text_color="red")
    




# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

#   App frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('SaveTube downloader - By Jawnchuks')


# adding UI element
title = customtkinter.CTkLabel(app, text="Insert a youtube link below")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url_var)
link.pack()

# finished downloading
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()

# progress bar
pPercent = customtkinter.CTkLabel(app, text="0%")
pPercent.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# download btn
download_btn = customtkinter.CTkButton(app, text="Download", command=startDownload)
download_btn.pack(pady=10)

# run app
app.mainloop()   
