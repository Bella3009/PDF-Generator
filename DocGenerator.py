from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("Titles.csv")

for index, row in df.iterrows():
    pdf.add_page()
    
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0,0,254) # Color Blu according RBG code
    
    # pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21) # To add a simple line

pdf.output("FirstPDF.pdf")
