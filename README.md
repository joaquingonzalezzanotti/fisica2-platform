# Fisica II - Estructura de proyecto


## Leer
-Instrucciones para el usuario final (inclúyelas en un README.txt):

Descomprimir el ZIP.
Doble clic a FinalFisica2.exe

## Raiz
- `index.html`: UI principal (sin build, HTML único).
- `assets/img/`: imágenes y favicon (`assets/img/favicon.png`).
- `inputs/`: material de curso.

## Inputs
- `inputs/modulos/modulo#`: PDFs y filminas por módulo (1..13).
  - `inputs/modulos/modulo#/filminas#`: PNG/PDF de filminas.
- `inputs/quiz/quizU#`: archivos JSON de quizzes (quizU#.json).
- `inputs/practicos/`: guías y ejercicios prácticos.
  - `inputs/practicos/practU#/practicos.json`: ejercicios interactivos por unidad.
- `inputs/Practico Fisica 2 2023.pdf`: guía general de prácticos.

## Notas
- Rutas relativas: todas las referencias en `index.html` apuntan a `inputs/...` y `assets/img/...`; mantener nombres al agregar contenido.
- Si se agrega CSS/JS externo, guardarlo en `assets/css` o `assets/js` y referenciarlo en `index.html`.
