from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.text = self.canvas.create_text(
            (150, 125),
            width=280,
            fill=THEME_COLOR,
            text="question here",
            font=("Ariel", 20, "italic")
        )

        self.score_label = Label(text=f"Score:{self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)


        false_button_image = PhotoImage(file="images/false.png")
        true_button_image = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, command=self.false_pressed)
        self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.true_pressed)
        self.false_button.grid(column=1, row=2)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.itemconfig(self.text, text=self.quiz.next_question())
            self.canvas.update()
        else:
            self.canvas.itemconfig(self.text, text="You reach the end of the quiz")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1


        else:
            self.canvas.config(bg="red")
        self.canvas.update()
        self.window.after(1000, func=self.get_next_question)





