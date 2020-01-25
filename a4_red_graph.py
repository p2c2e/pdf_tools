from fpdf import FPDF
 
def draw_lines():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_draw_color(255, 0, 0)
    pdf.set_line_width(0.05)
    margin=10
    width=pdf.w
    height=pdf.h
    for i in range(0,(int) (width-2*margin)):
        pdf.line(margin+i, margin, margin+i, (int) (height-margin))
    for i in range(0,(int) (height-2*margin)):
        pdf.line(margin, margin+i, (int) (width-margin), margin+i)
    pdf.set_line_width(0.15)
    for i in range(0,(int) (width-2*margin),10):
        pdf.line(margin+i, margin, margin+i, (int) (height-margin))
    for i in range(0,(int) (height-2*margin),10):
        pdf.line(margin, margin+i, (int) (width-margin), margin+i)
    pdf.output('a4_red.pdf')
 
if __name__ == '__main__':
    draw_lines()
