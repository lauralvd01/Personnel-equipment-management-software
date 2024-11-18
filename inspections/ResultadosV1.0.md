1. Security
- 2 Open Issues:
	-	Hay dos vulnerabilidades de seguridad en el proyecto que necesitan ser revisadas. Estas podrían ser problemas como inyección de dependencias, uso de bibliotecas desactualizadas o configuraciones inseguras.
	-	Acción Tomada: Se examinó el análisis de sonarqube y se concluye en modifar o quitar del codigo "Django Secret Key", en la carpeta Seguridad se encuentra el error

- 21 Security Hotspots:
	-	Los security hotspots son puntos en el código donde se requiere una revisión manual para confirmar si representan un riesgo de seguridad.
	-	Acción Tomada: Revisamos los Hotspots del código y se basan en acciones en cuanto a "sugerencias" de HTML, adjuntos en la carpeta Hotspot, por lo que ninguna acción será tomada.

2. Reliability

- 34 Open Issues:
	-	Esto refleja posibles errores que pueden afectar la estabilidad del Software.
	-	Calificación: “C” indica que la fiabilidad del código puede mejorar.
	-	Acción Tomada: Identificamos que solo hay un archivo que genera problemas en el código, adjunto en la carpeta Reliability, se tomaran acciones para mejorar el archivo, el resto de lo 44 archivo analizadods no se encontraron problemas y pasaron la prueba con una A.

3. Maintainability

- 65 Open Issues:
	-	Los problemas de mantenibilidad suelen estar relacionados con la complejidad del código, duplicación o estructuras mal diseñadas que dificultan su comprensión y modificación.
	-	Calificación: “A” es una muy buena nota, indicando que aunque hay problemas, la mantenibilidad general del código es alta.
	-	Acción Tomada: Revisamos los 65 problemas y concluimos que las acciones recomendadas eran lineas no cubiertas por tests.

4. Coverage

- 0.0% de Cobertura:
	-	Esto indica que no hay pruebas automatizadas cubriendo tu código.
	-	Impacto: La falta de cobertura de pruebas hace que el código sea más propenso a errores al introducir cambios o nuevas funcionalidades.
	-	Acción Tomada: Implementaremos pruebas unitarias y de integración para asegurar que el código sea verificable.

5. Duplications

- 0.0% de Duplicaciones:
	-	Este es un buen resultado, lo que significa que el código no tiene secciones repetidas innecesariamente.

6. Quality Gate

- Passed:
	-	Esto significa que el proyecto cumple con los criterios de calidad mínimos establecidos en SonarCloud.