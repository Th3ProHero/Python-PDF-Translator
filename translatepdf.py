import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
from tkinter import Tk, filedialog

# Función para dividir texto en partes más pequeñas
def split_text(text, max_length=5000):
    paragraphs = text.split("\n")  # Dividir por líneas
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

# Función para extraer texto de un PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# Función para traducir texto
def translate_text(text, target_language="es"):
    translator = GoogleTranslator(source='auto', target=target_language)
    chunks = split_text(text)  # Dividir texto en partes
    translated_chunks = [translator.translate(chunk) for chunk in chunks]
    return "\n".join(translated_chunks)

# Función para crear un nuevo PDF traducido
def create_translated_pdf(output_path, translated_text):
    doc = fitz.open()  # Crear un documento PDF vacío
    page = doc.new_page()  # Añadir una página
    page.insert_text((50, 50), translated_text)  # Añadir texto traducido
    doc.save(output_path)
    doc.close()

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

    # Procesar y traducir
    print("Extrayendo texto...")
    original_text = extract_text_from_pdf(input_pdf_path)

    print("Traduciendo texto...")
    translated_text = translate_text(original_text)

    print("Creando PDF traducido...")
    create_translated_pdf(output_pdf_path, translated_text)

    print(f"PDF traducido guardado en: {output_pdf_path}")

# Ejecutar función principal
if __name__ == "__main__":
    main()