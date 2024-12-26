# PDF Translator: Traducción Automática de PDFs con Respeto al Formato

Este proyecto tiene como objetivo traducir textos de un archivo PDF de un idioma a otro, respetando el formato original en la medida de lo posible. La traducción se realiza utilizando la API de Google Translate, y el texto traducido se inserta en las mismas posiciones de la página que el texto original, manteniendo la mayor parte del formato, fuentes y colores.

## Avances del Proyecto

### 1. **Primera Versión (Versión Inicial)**
En la primera versión del código, se logró lo siguiente:
- **Extracción de texto**: Utilizando `PyMuPDF`, se extrajo el texto del PDF respetando las posiciones y los bloques de texto.
- **Traducción**: El texto extraído se tradujo usando la API de Google Translate.
- **Reemplazo de texto**: El texto traducido se insertó en el mismo lugar en la página, cubriendo el texto original.

Problema: El texto traducido se insertaba encima del texto original, lo que resultaba en una superposición no deseada.

### 2. **Segunda Versión (Mejora en el Formato)**
Se mejoró el código para:
- **Eliminar el texto original**: El texto original fue cubierto por un rectángulo blanco antes de insertar el texto traducido, lo que evitó la superposición.
- **Mejorar el ajuste de texto**: Se añadió lógica para verificar que el texto traducido no se desbordara de los márgenes de la página. Si el texto era largo, se ajustaba dinámicamente el tamaño de la fuente.

Problema: Algunas partes del texto se seguían saliendo de los márgenes y la posición de algunos bloques de texto seguía siendo imperfecta.

### 3. **Versión Final (Ajuste de Formato y Tamaño de Fuente)**
En esta versión final, se implementaron los siguientes avances:
- **Ajuste dinámico de la posición**: Se añadieron controles adicionales para asegurar que el texto traducido se mantenga dentro de los márgenes de la página.
- **Ajuste dinámico del tamaño de la fuente**: El tamaño de la fuente se ajusta si el texto traducido es más largo que el original, asegurando que todo el texto se ajuste dentro de su espacio correspondiente sin desbordarse.
- **Mejor control sobre el formato**: El código ahora puede manejar mejor el formato, como el color del texto y la fuente.

### Funcionalidad alcanzada:
- **Extracción precisa del texto** de un PDF.
- **Traducción automática** de cualquier texto de un archivo PDF.
- **Reemplazo del texto** en el PDF con el texto traducido, respetando las posiciones y las fuentes.
- **Ajuste de la fuente** para evitar que el texto se desborde.

## Instalación

Para ejecutar este proyecto, necesitas tener instalado Python 3.7+ y algunas librerías externas. Puedes instalar las dependencias necesarias usando `pip`.

```bash
pip install PyMuPDF deep-translator
