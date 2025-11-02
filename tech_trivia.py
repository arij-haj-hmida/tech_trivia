import tkinter as tk
import random

class TechTrivia:
    def __init__(self, root):
        self.root = root
        self.root.title("💻 Tech Trivia")
        self.root.geometry("500x400")
        self.root.configure(bg="#E8F5E9")

        self.questions = [
            ("Who founded Microsoft?", ["Steve Jobs", "Bill Gates", "Elon Musk", "Larry Page"], "Bill Gates"),
            ("What does CPU stand for?", ["Central Processing Unit", "Core Program Utility", "Central Power Unit", "Computer Processing Unit"], "Central Processing Unit"),
            ("Which programming language has a snake logo?", ["Python", "Java", "C++", "Ruby"], "Python"),
            ("HTML is used to create what?", ["Web Pages", "Databases", "Games", "APIs"], "Web Pages"),
            ("What year was the first iPhone released?", ["2005", "2007", "2009", "2010"], "2007"),
        ]
        random.shuffle(self.questions)
        self.index = 0
        self.score = 0
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="💻 Tech Trivia!", font=("Arial", 20, "bold"), bg="#E8F5E9", fg="#333").pack(pady=20)
        self.q_label = tk.Label(self.root, text="", wraplength=450, font=("Arial", 14), bg="#E8F5E9")
        self.q_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", width=30, height=2, bg="#C8E6C9", command=lambda i=i: self.check(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.next_btn = tk.Button(self.root, text="Next", bg="#81C784", fg="white", command=self.next_q, state=tk.DISABLED)
        self.next_btn.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score: 0", bg="#E8F5E9", font=("Arial", 12))
        self.score_label.pack()

        self.load_q()

    def load_q(self):
        q, opts, _ = self.questions[self.index]
        self.q_label.config(text=q)
        for i, o in enumerate(opts):
            self.buttons[i].config(text=o, bg="#C8E6C9", state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)

    def check(self, i):
        correct = self.questions[self.index][2]
        if self.buttons[i].cget("text") == correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.buttons[i].config(bg="#A5D6A7")
        else:
            self.buttons[i].config(bg="#FF9B9B")
        for b in self.buttons:
            b.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL)

    def next_q(self):
        self.index += 1
        if self.index < len(self.questions):
            self.load_q()
        else:
            self.result()

    def result(self):
        for w in self.root.winfo_children():
            w.destroy()
        tk.Label(self.root, text=f"🏁 Game Over!\nScore: {self.score}/{len(self.questions)}", bg="#E8F5E9",
                 font=("Arial", 18, "bold")).pack(pady=50)
        tk.Button(self.root, text="Play Again", command=self.restart, bg="#81C784", fg="white").pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#FF7070", fg="white").pack()

    def restart(self):
        for w in self.root.winfo_children():
            w.destroy()
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    TechTrivia(root)
    root.mainloop()
