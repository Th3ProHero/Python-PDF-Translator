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
    translated_chunks = []
    
    for chunk in chunks:
        try:
            translated_text = translator.translate(chunk)
            if translated_text:  # Verificar que la traducción no sea None
                translated_chunks.append(translated_text)
            else:
                translated_chunks.append(chunk)  # Si no se traduce, se mantiene el texto original
        except Exception as e:
            print(f"Error al traducir el texto: {e}")
            translated_chunks.append(chunk)  # En caso de error, mantener el texto original

    return "\n".join(translated_chunks)

# Función para traducir y conservar formato en cada página
def translate_pdf_while_preserving_format(input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)  # Abrir PDF de entrada
    for page_num in range(len(doc)):
        print(f"Procesando página {page_num + 1} de {len(doc)}...")
        page = doc[page_num]

        # Extraer bloques de texto con su formato
        text_blocks = page.get_text("dict")["blocks"]
        for block in text_blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        original_text = span["text"]
                        if original_text.strip():  # Traducir solo si hay texto
                            translated_text = translate_text(original_text)

                            # Establecer color negro (0, 0, 0)
                            color = (0, 0, 0)

                            # Reemplazar texto con fuente helv (Helvetica) y color negro
                            page.insert_text(
                                (span["bbox"][0], span["bbox"][1]),  # Coordenadas originales
                                translated_text,
                                fontsize=span["size"],  # Tamaño de fuente original
                                color=color,  # Color negro
                                fontname="helv"  # Fuente helv (Helvetica)
                            )

    # Guardar el PDF traducido
    doc.save(output_pdf_path)
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

    # Traducir PDF respetando formato
    translate_pdf_while_preserving_format(input_pdf_path, output_pdf_path)

# Ejecutar función principal
if __name__ == "__main__":
    main()
