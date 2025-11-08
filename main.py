from docxtpl import DocxTemplate

doc = DocxTemplate("Invoice_Template_rows_fixed.docx")

items = [
    {"desc": "pen", "qty": 2, "price": 0.5, "total": 1.0},
    {"desc": "notebook", "qty": 1, "price": 3.0, "total": 3.0},
    {"desc": "eraser", "qty": 3, "price": 0.2, "total": 0.6},
]

context = {
    "name": "Bhavika",
    "email": "bhavika@example.com",
    "invoice_list": items,
    "total": sum(i["total"] for i in items),
}

doc.render(context)
doc.save("new_invoice.docx")

