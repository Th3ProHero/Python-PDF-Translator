import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
from tkinter import Tk, filedialog

# Función para dividir texto en partes pequeñas
def split_text(text, max_length=5000):
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 1 > max_length:
            chunks.append(current_chunk)
            current_chunk = paragraph
        else:
            current_chunk += "\n" + paragraph

    if current_chunk:
        chunks.append(current_chunk)
    return chunks

# Función para traducir texto
def translate_text(text, target_language="es"):
    translator = GoogleTranslator(source='auto', target=target_language)
    chunks = split_text(text)  # Dividir texto en partes
    translated_chunks = [translator.translate(chunk) for chunk in chunks]
    return "\n".join(translated_chunks)

# Función para traducir cada página del PDF
def translate_pdf_by_page(input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)  # Abrir PDF de entrada
    new_doc = fitz.open()  # Crear un nuevo documento PDF

    for page_num in range(len(doc)):
        print(f"Traduciendo página {page_num + 1} de {len(doc)}...")
        page = doc[page_num]
        original_text = page.get_text()  # Extraer texto de la página
        translated_text = translate_text(original_text)  # Traducir texto

        # Crear una nueva página en el documento traducido
        new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)

        # Insertar texto traducido en la nueva página
        new_page.insert_text((50, 50), translated_text)  # Ajustar posición según necesidad

    # Guardar el PDF traducido
    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()
    print(f"PDF traducido guardado en: {output_pdf_path}")

# Función principal con selección de archivos
def main():
    # Configurar Tkinter
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Seleccionar archivo PDF de entrada
    input_pdf_path = filedialog.askopenfilename(
        title="Selecciona el archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    if not input_pdf_path:
        print("No se seleccionó ningún archivo.")
        return

    # Seleccionar archivo PDF de salida
    output_pdf_path = filedialog.asksaveasfilename(
        title="Guardar PDF traducido como",
        defaultextension=".pdf",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    if not output_pdf_path:
        print("No se seleccionó un lugar para guardar el archivo.")
        return

    # Traducir PDF página por página
    translate_pdf_by_page(input_pdf_path, output_pdf_path)

# Ejecutar función principal
if __name__ == "__main__":
    main()
