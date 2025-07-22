from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Developer Team | Face Recognition System")
        self.root.config(bg="#0f1e4d")  # Background: Navy Blue

        # Title
        title_lbl = Label(self.root, text="👨‍💻 Meet the Developers", font=('Helvetica', 38, 'bold'),
                          bg="#0f1e4d", fg='cyan')
        title_lbl.pack(pady=(20, 5))

        # Clean project summary (no special Unicode)
        summary_text = (
            "Face Recognition Student Attendance System is an automated application built using OpenCV, "
            "Tkinter, and MySQL. It enables students' face data registration, model training, attendance "
            "marking via real-time facial recognition, and attendance logging in a database. This system improves "
            "accuracy, security, and automation in attendance tracking for educational institutions."
        )

        summary_lbl = Label(
            self.root,
            text=summary_text,
            wraplength=1350,
            justify="left",
            font=("Helvetica", 14, "bold"),
            bg="#0f172a",
            fg="white",
            padx=20,
            pady=15
        )
        summary_lbl.place(x=20, y=60, width=1460, height=110)


        # Developer data
        team = [
            {
                "img": "/Users/yashrawat/Desktop/Face_Recognition_System/images/yash.jpg",
                "name": "Yash Rawat",
                "designation": "Lead Developer",
                "role": "Face Recognition, GUI Integration, DB Logging",
                "summary": "Expert in Python & Computer Vision. Built smart, seamless systems.",
                "email": "yashrawat2362@gmail.com",
                "linkedin": "https://www.linkedin.com/in/yashrawat2362",
                "github": "https://github.com/yashrawat2362"
            },
            {
                "img": "/Users/yashrawat/Desktop/Face_Recognition_System/images/harsh.jpg",
                "name": "Harsh Tongar",
                "designation": "ML Engineer",
                "role": "Dataset Preparation, Training Module",
                "summary": "Machine Learning enthusiast with strong data skills.",
                "email": "harshtongar@example.com",
                "linkedin": "https://www.linkedin.com/in/harsh-tongar",
                "github": "https://github.com/harsh-tongar"
            },
            {
                "img": "/Users/yashrawat/Desktop/Face_Recognition_System/images/hemant.jpg",
                "name": "Hemant",
                "designation": "QA & Automation",
                "role": "Testing, Excel Automation, Review",
                "summary": "Focused on automation, testing, and smooth workflows.",
                "email": "hemant@example.com",
                "linkedin": "https://www.linkedin.com/in/hemant-dev",
                "github": "https://github.com/hemant-dev"
            }
        ]

        cards_frame = Frame(self.root, bg="#0f1e4d")
        cards_frame.place(x=50, y=160, width=1400, height=560)

        x_offset = 50
        for dev in team:
            self.create_card(cards_frame, dev, x_offset)
            x_offset += 440

        back_btn = Button(
        self.root,
        text="← Back to Main Menu",
        command=self.root.destroy,
        font=("Helvetica", 14, "bold"),
        bg="#1e40af",        # Navy Blue background
        fg="black",          # White text
        activebackground="#1e3a8a",  # Darker blue on hover/click
        activeforeground="white",
        bd=0,
        relief=RIDGE,
        cursor="hand2"
        )
        back_btn.place(x=20, y=720, width=200, height=40)


    def create_card(self, parent, dev, x):
        card = Frame(parent, bg="#162a5d", bd=2, relief="ridge")
        card.place(x=x, y=10, width=400, height=530)

        try:
            img = Image.open(dev["img"])
        except:
            img = Image.new('RGB', (160, 160), color='gray')
        img = img.resize((150, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        img_lbl = Label(card, image=photo, bg="#162a5d")
        img_lbl.image = photo
        img_lbl.place(x=125, y=10)

        Label(card, text=dev["name"], font=("Helvetica", 18, "bold"), bg="#162a5d", fg="cyan").place(x=0, y=170, width=400)
        Label(card, text=dev["designation"], font=("Helvetica", 14, "italic"), bg="#162a5d", fg="#d1d1d1").place(x=0, y=200, width=400)

        Label(card, text="🛠️ Role:", font=("Helvetica", 13, "bold"), bg="#162a5d", fg="white", anchor="w").place(x=20, y=240)
        Label(card, text=dev["role"], font=("Helvetica", 12), bg="#162a5d", fg="#e6e6e6",
              wraplength=360, justify=LEFT).place(x=20, y=265)

        Label(card, text="📄 Summary:", font=("Helvetica", 13, "bold"), bg="#162a5d", fg="white", anchor="w").place(x=20, y=315)
        Label(card, text=dev["summary"], font=("Helvetica", 12), bg="#162a5d", fg="#e6e6e6",
              wraplength=360, justify=LEFT).place(x=20, y=340)

        Label(card, text=f"📧 {dev['email']}", font=("Helvetica", 11), bg="#162a5d", fg="#d9edf7").place(x=20, y=400)

        linkedin_lbl = Label(card, text="🔗 LinkedIn", font=("Helvetica", 11, "underline"),
                             bg="#162a5d", fg="skyblue", cursor="hand2")
        linkedin_lbl.place(x=20, y=430)
        linkedin_lbl.bind("<Button-1>", lambda e: webbrowser.open(dev["linkedin"]))

        github_lbl = Label(card, text="🐙 GitHub", font=("Helvetica", 11, "underline"),
                           bg="#162a5d", fg="skyblue", cursor="hand2")
        github_lbl.place(x=130, y=430)
        github_lbl.bind("<Button-1>", lambda e: webbrowser.open(dev["github"]))

        Label(card, text="🚀 Innovating smarter solutions together!", font=("Helvetica", 11, "bold"),
              fg="lightgreen", bg="#162a5d").place(x=30, y=470)

if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()
