from fpdf import FPDF

class PDF(FPDF):

    def top(self):
        self.image("shirtificate.png", 10, 65, 190, 190)
        self.set_font("helvetica", "B", 45)
        self.text(45, 45, "CS50 Shirtificate")

    def label(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.text(70, 145, t + "took CS50")

t = input("What's your name? ").strip()
filepdf = PDF()
filepdf.add_page()
filepdf.output("shirtificate.pdf")