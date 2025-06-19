# Proyecto Sala Reservas - Grupo 5

**Integrantes:**  
- Juan Villaman  
- Cristóbal de Jesús  
- Víctor Figueroa  

---

## Descripción

Este proyecto implementa un sistema básico para gestionar reservas de salas de reuniones en un entorno ágil. Aplicamos principios de Agile Testing y Desarrollo Guiado por Pruebas (TDD), creando primero pruebas unitarias y de integración para garantizar calidad y funcionalidad desde el inicio. Además, automatizamos la ejecución de pruebas mediante GitHub Actions, integrándolo en un pipeline CI/CD.

---

## Diferencias entre Agile Testing y enfoque tradicional

La principal diferencia con el enfoque tradicional es que Agile Testing integra las pruebas desde el inicio y de forma continua, como hicimos creando tests antes del código con TDD y automatizando su ejecución en CI/CD.

---

## Ventajas y desafíos del uso de TDD

Usar TDD nos permitió escribir solo el código necesario para pasar pruebas, lo que mejora calidad y reduce errores. Lo más complejo fue pensar primero en los casos de prueba antes de implementar la lógica.

---

## Tipo de prueba que más valor aportó

Las pruebas de integración aportaron gran valor, porque validaron el comportamiento real de la API de reservas, asegurando que la lógica y la comunicación HTTP funcionaran correctamente juntas.

---

## Mantenimiento de la suite de pruebas

Mantendríamos la suite actualizando y agregando pruebas con cada cambio, además de automatizar la ejecución continua con GitHub Actions para detectar fallos tempranamente y garantizar calidad constante.

---

## Tecnologías y herramientas usadas

- Python 3.10+
- Flask para la API REST
- Pytest para pruebas unitarias y de integración
- GitHub Actions para automatización y CI/CD

---

## Cómo ejecutar el proyecto localmente

1. Crear y activar entorno virtual  
2. Instalar dependencias con `pip install -r requirements.txt`  
3. Ejecutar pruebas con `pytest`  

---

Gracias por revisar nuestro trabajo.  
Grupo 5 - Sala Reservas.
