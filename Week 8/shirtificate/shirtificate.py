from fpdf import FPDF


def main():
    name = input("Enter your name: ")
    create_shirtificate(name, "shirtificate.png")


def create_shirtificate(name, image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")
    pdf.image(image_path, x=(210 - pdf.epw) / 2, y=60, w=pdf.epw)
    pdf.set_xy(10, 140)
    pdf.set_font_size(32)
    pdf.set_text_color(255, 255, 255)
    pdf.multi_cell(0, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
