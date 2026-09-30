# Prompts para clasificar y seleccionar noticias en Copilot (SharePoint)

Mensajes listos para pegar en el chat de Copilot de una biblioteca de SharePoint que tenga noticias, una por fichero. Cada fichero es el texto exacto, sin encabezados.

```
clasificar/    01-crear-columnas.md  ->  02-rellenar-y-auditar.md  ->  03-comprobar.md
seleccionar/   01-seleccionar-con-columnas.md
```

## Cómo se usa
1. Abre la biblioteca y el chat de Copilot.
2. Pega un mensaje cada vez, en el orden de los números. Copilot te pedirá confirmar antes de actualizar elementos.
3. Comprueba el resultado: los motivos los escribe leyendo cada documento y puede equivocarse.

## Qué puedes cambiar
- **Clasificar:** las categorías y subcategorías del mensaje 1. Son las del boletín de AVRA; pon las tuyas.
- **Seleccionar:** los cinco criterios de la lista y el tope de 15.

## Qué se ha probado
- **Seleccionar:** probado. Creó las columnas «Seleccionada» y «Motivo de selección», las rellenó y dejó 15 en «Sí». Un criterio del tipo «todo lo que no sea…» no funcionó en nuestra prueba: el chat respondió con texto y no dejó nada en la biblioteca. Escribe el criterio en positivo («marca Sí si…»).
- **Clasificar:** la versión básica (solo Categoría y Subcategoría) se probó y clasificó los 100 documentos. Esta versión ampliada, con las columnas «Motivo» y «Revisar», **aún no se ha probado**: revisa qué hace antes de fiarte.

Esto clasifica y selecciona dentro de SharePoint; no es un agente.
