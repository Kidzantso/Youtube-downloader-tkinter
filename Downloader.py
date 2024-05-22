import tkinter as tk
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox, filedialog
import re

def browseFiles():
    #function browse uses filedialog from tkinter to choose a directory to save the video in it
	filename = filedialog.askdirectory(initialdir = "/",title = "Select a Folder")
	folder_path.set(filename)
   
def Resolutions():
    #function resolutions show the resolutions and mime type and fps of the video
    #and put them in the combo box so the user can choose what he wants
    #either audio or video,if you want to see other parameters than shown just 
    #add print(i) on line 22
    Youtube_link = linkText.get()
    if Youtube_link=="":messagebox.showinfo("Failed","No URL was entered");return #shows error if no url was entered
    getVideo = YouTube(Youtube_link)
    for i in getVideo.streams:
        if(i.resolution!=None): #for video type showing resolution and fps and coding because not all coding formats are supported
            current_options = combo["values"]
            updated_options = list(current_options) + [str("Tag: "+str(i.itag)+" Resolution: "+i.resolution+" Type: "+i.mime_type+" FPS: "+str(i.fps)+" coding: "+str(i.codecs))]  # Add them to the combo box
            combo["values"] = updated_options
        else: #for audio type showing abr and coding because not all coding formats are supported
            current_options = combo["values"]
            updated_options = list(current_options) + [str("Tag: "+str(i.itag)+" ABR: "+i.abr+" Type: "+i.mime_type+" coding: "+str(i.codecs))]  # Add them to the combo box
            combo["values"] = updated_options
def Download():
	Youtube_link = linkText.get()
	if Youtube_link=="":messagebox.showinfo("Failed","No URL was entered");return #check url entered
	download_Folder = destinationText.get()
	if download_Folder=="":messagebox.showinfo("Failed","No Destination was entered");return #check if a directory is chosen
	getVideo = YouTube(Youtube_link)
	if combo.get()=="":messagebox.showinfo("Failed","Choose a resolution first");return #check if the user selected an option
	tag_number = re.search(r'\d+', combo.get()).group() #get the tag number from the combox
	videoStream = getVideo.streams.get_by_itag(tag_number) #download by using the tag number
	match = re.search(r'/(?P<word>\w+)', combo.get()) #get tye type after the / to add it to the extension
	if match:
		word_after_slash = match.group("word")
	if Nametext.get()=="": #if no name entered it is downloaded with the same video name
		if videoStream.download(download_Folder):
			messagebox.showinfo("Success","Saved in\n"+ download_Folder) #check if downloaded successfully
		else:messagebox.showinfo("Failed","Failed to download,Try again") #show error if not downloaded successfully
	else: #if a specific name chosen it is written then addded the extension that we got from words after slash
		if videoStream.download(output_path=download_Folder,filename=Nametext.get()+"."+word_after_slash):
				messagebox.showinfo("Success","Saved in\n"+ download_Folder) #check if downloaded successfully
		else:messagebox.showinfo("Failed","Failed to download,Try again") #show error if not downloaded successfully

# putting widgets on the screen
root = tk.Tk()
folder_path = StringVar()
head_label = Label(root, text="YouTube Video Downloader",padx=15,pady=15,font="SegoeUI 14",bg="red",fg="white")
head_label.grid(row=1,column=1,pady=10,padx=5,columnspan=3)
link_label = Label(root,text="YouTube link :",bg="#5A47A5",pady=5,padx=5)
link_label.grid(row=2,column=0,pady=5,padx=5)
linkText = Entry(root,width=35,font="Arial 14")
linkText.grid(row=2,column=1,pady=5,columnspan=2)
destination_label = Label(root,text="Destination :",bg="#5A47A5",pady=5,padx=9)
destination_label.grid(row=3,column=0,pady=5,padx=5)
Name_label = Label(root,text="Choose Name for the video :",bg="#5A47A5",pady=5,padx=9)
Nametext = Entry(root,width=35,font="Arial 14")
Nametext.grid(row=4,column=1,pady=5,columnspan=2)
Name_label.grid(row=4,column=0)
combo = ttk.Combobox(root,width=80,state="readonly")
combo["values"] = []
combo.grid(row=7,column=1,pady=2)
destinationText = Entry(root,width=27,font="Arial 14",textvariable=folder_path)
destinationText.grid(row=3,column=1)
browse_B = Button(root,text="Browse",command=browseFiles,width=10,bg="#6D2061", activebackground="#6D2061")
browse_B.grid(row=3,column=2)
Download_B = Button(root,text="Download Video",command=Download,width=10,bg="#3401FF", activebackground="#3401FF",pady=10,padx=10)
Download_B.grid(row=6,column=1,pady=2)
Resolution_label = Label(root,text="Choose type and resolution :",bg="#5A47A5",pady=5,padx=9)
Resolution_label.grid(row=7,column=0)
Resolutions_b = Button(root,text="Show Resolutions",command=Resolutions,width=10,bg="#CCA62C", activebackground="#CCA62C",pady=10,padx=10)
Resolutions_b.grid(row=5,column=1,pady=2)


root.geometry("750x350")
root.resizable(width=False,height=False)
root.configure(bg="#5A47A5")
root.title("YouTube Video Downloader")
root.mainloop()
