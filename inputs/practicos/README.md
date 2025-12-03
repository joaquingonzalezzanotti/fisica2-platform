Formato sugerido para ejercicios prácticos por módulo (uno por carpeta `practU#`):

```
inputs/practicos/practU1/practicos.json
inputs/practicos/practU2/practicos.json
...
```

Ejemplo de `practicos.json`:

```json
{
  "moduleId": "u2",
  "title": "Prácticos Unidad 2",
  "exercises": [
    {
      "id": "u2-e01",
      "title": "Trabajo en proceso isobárico",
      "statement": "Un mol de gas ideal se expande isobáricamente de 2 L a 6 L a 1 atm. Calcula el trabajo realizado y el calor si ΔT = 120 K.",
      "hint": "W = -P ΔV; usa primera ley con ΔE = n Cv ΔT.",
      "solution": "W ≈ -405 J; con Cv ≈ 5/2 R, Q ≈ 5/2 R ΔT + 405 J.",
      "tags": ["termodinamica", "isobarico", "trabajo", "primera_ley"],
      "difficulty": "media",
      "source": {
        "pdf": "inputs/Practico Fisica 2 2023.pdf",
        "section": "Sección 3 (Transformaciones en gases)",
        "page": 20
      }
    }
  ]
}
```

Campos:
- `moduleId`: u1...u13.
- `exercises`: array de ejercicios.
  - `id`: identificador único.
  - `title`: título breve.
  - `statement`: enunciado completo.
  - `hint`: pista opcional.
  - `solution`: breve solución o pasos.
  - `tags`: etiquetas para filtrar.
  - `difficulty`: baja | media | alta.
  - `source`: referencia opcional al PDF general (`pdf`, `section`, `page`).
