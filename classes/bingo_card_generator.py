from classes.bingo import Bingo
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image

class BingoCardGenerator:

    def generate_pdf(self, center_image_path: str, number_of_cards=1,filename="bingo_card.pdf"):
        
        
        elements = [Spacer(0.2, 0.2 * cm)]
        
        for _ in range(number_of_cards):
            bingo_card = Bingo().get_bingo_card()
            data = [bingo_card.keys()]
            
            for i in range(5):
                row = []
                for letter in bingo_card.keys():
                    value = bingo_card[letter][i]
                    if value == 'special':
                        img = Image(center_image_path, width=2.5*cm, height=2.5*cm)
                        row.append(img)
                    else:
                        row.append(str(value))
                data.append(row)
            
            doc = SimpleDocTemplate(filename, pagesize=(13 * cm, 16 * cm), leftMargin=0.5 * cm, rightMargin=0.5 * cm, topMargin=0 * cm, bottomMargin=0 * cm)
            table = Table(data, colWidths=2.5 * cm, rowHeights=2.5 * cm)
            
            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), 
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), 
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 16),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])
            table.setStyle(style)
            
            elements.append( table)
        doc.build(elements)
        print(f"PDF '{filename}' generated successfully!")
