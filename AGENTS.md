# Instrucciones para Jules (Agente de IA)

Siempre que detectes un nuevo Pull Request o cambios en este repositorio:

1. **Documentación Automática:** - Genera docstrings para cada clase y función nueva en `models.py` y `views.py`.
   - Los comentarios deben estar en español técnico.

2. **Control de Errores (Robustez):**
   - Si añades lógica de base de datos, asegura que existan bloques `try-except`.
   - Verifica que los modelos de Django tengan validaciones adecuadas.

3. **Testing:**
   - Si creo una nueva funcionalidad, genera automáticamente un archivo `tests.py` (o actualiza el existente) con pruebas unitarias básicas.

4. **Revisión de Estilo:**
   - Asegúrate de que el código siga las normas PEP 8 de Python.