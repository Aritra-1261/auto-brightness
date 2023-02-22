import customtkinter as ck
import brightness_control as bc

ck.set_appearance_mode("system")
ck.set_default_color_theme("dark-blue")

root=ck.CTk()
root.title("Auto Brightness")
root.geometry("300x150")

frame=ck.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=ck.CTkLabel(master=frame,text="Auto Brightness",font=("Roboto",24,"bold"))
label.pack(pady=12)

button=ck.CTkButton(master=frame,text="Auto Adjust",command=bc.auto)
button.pack(pady=12)

root.mainloop()

