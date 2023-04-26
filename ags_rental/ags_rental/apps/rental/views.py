import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render


def rental_view(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()

    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename='hello.pdf')
