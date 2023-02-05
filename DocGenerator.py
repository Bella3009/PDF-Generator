from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("Titles.csv")

for index, row in df.iterrows():
    pdf.add_page()
    
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0,0,254) # Color Blu according RBG code
    
    # pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # .line(x1, y1, x2, y2) x rapresent the horizontal line while y is vertical. 1 is from the left and 2 from the right
    
    pdf.line(10, 21, 200, 21) # To add a simple line
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    
    for i in range(row["Pages"]-1):
        pdf.add_page()
        
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("FirstPDF.pdf")
