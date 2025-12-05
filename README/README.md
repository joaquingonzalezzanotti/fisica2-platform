# Fisica II - Proyecto offline

## Como arrancar
- Opcion 1 (recomendada): doble clic a `run_server.exe` en la raiz, acepta el aviso de firewall si aparece, y se abre `http://127.0.0.1:5500/index.html`.
- Opcion 2 (fallback con Python instalado): doble clic a `run.bat` o ejecuta en consola `python -m http.server 5500` dentro de la carpeta. Abre `http://localhost:5500/index.html`.

## Contenido
- `index.html`: UI principal (sin build).
- `assets/img/`: favicon y formulas (`assets/img/formulas/`; solo `u1.png` incluida).
- `inputs/`: material de curso.
  - `inputs/modulos/modulo#/` (1..13) con PDFs y subcarpetas `filminas#`.
  - `inputs/quiz/quizU#/` con `quizU#.json`.
  - `inputs/practicos/practU#/` con `practicos.json`.
  - PDFs generales: `inputs/Practico Fisica 2 2023.pdf`, `inputs/Programa de Fisica 2.pdf`.
- Herramientas: `run_server.exe` (server embebido) y `run_server.py` (fuente del servidor).

## Notas
- Mantener nombres y rutas relativas (`inputs/...`, `assets/img/...`) para que el HTML encuentre los archivos.
- Si agregas mas imagenes de formulas, seguir el nombre `assets/img/formulas/u#.png`.
- Si no se abre automaticamente el navegador, abre manualmente `http://127.0.0.1:5500/index.html` mientras el servidor este corriendo.
