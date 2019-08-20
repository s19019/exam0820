import tkinter as tk

class Question(tk.Frame):
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = tk.Label(view, text="わっさ！")
            right += 1
        else:
            label = tk.Label(view, text="アホかな？")

        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, root):
        view = tk.Frame(root)
        label = tk.Label(view, text=self.question)
        button_a = tk.Button(view, text=self.answers[0], command=lambda *args: self.check("A", view))
        button_b = tk.Button(view, text=self.answers[1], command=lambda *args: self.check("B", view))
        button_c = tk.Button(view, text=self.answers[2], command=lambda *args: self.check("C", view))
        button_d = tk.Button(view, text=self.answers[3], command=lambda *args: self.check("D", view))
        label.pack()
        button_a.pack()
        button_b.pack()
        button_c.pack()
        button_d.pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, root, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        tk.Label(root, text="やったね！ " + str(right) + "/" + str(number_of_questions) + "全てが答えでハズレだよ、ハハッ!").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(root).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

root = tk.Tk()
root.title("なっきー")
button = tk.Button(root, text="今日も来てくれて、ありがとう！", command=askQuestion)
button.pack()
root.geometry('750x400+0+0')
root.mainloop()
