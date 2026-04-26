# 🗺️ EFT.node - Escape From Tarkov Quest Visualizer

EFT.node es un visualizador de grafos interactivo y ultrarrápido para las misiones de Escape From Tarkov. Diseñado para ser una herramienta de consulta pura, permite a los jugadores explorar el árbol de misiones, ver requisitos y planificar su wipe sin tiempos de carga.

## ✨ Características Principales

* **Carga Cero (Zero-Latency):** El grafo se renderiza instantáneamente utilizando una base de datos local (`default_tasks.json`), sin depender de llamadas a servidores en el primer impacto.
* **Sincronización en Vivo (Live Fetch):** ¿Sospechas que hubo un parche silencioso o un wipe? Un botón dedicado hace una consulta GraphQL a la API de `tarkov.dev` para reconstruir el grafo con los datos más recientes en tiempo real.
* **Grafo Interactivo:** Construido con React Flow para permitir zoom, paneo y exploración fluida de los nodos (misiones) y sus conexiones (prerrequisitos).
* **Consulta Pura:** Sin sistema de cuentas ni guardado de progreso. Entras, miras lo que necesitas saber y vuelves a la incursión.

## 🏗️ Arquitectura y Tecnologías

El proyecto sigue una arquitectura *Serverless* / Frontend-only para garantizar un coste de alojamiento nulo y un mantenimiento mínimo:

* **Frontend:** React (TypeScript/JavaScript).
* **Motor del Grafo:** React Flow.
* **Estilos:** TailwindCSS.
* **Fuente de Datos:** `tarkov.dev/api` (vía GraphQL).
* **Despliegue Recomendado:** Vercel o GitHub Pages.

## 🚀 Instalación y Uso (Desarrollo Local)

### 1. Levantar el Frontend web
Clona el repositorio e instala las dependencias para hacer correr el visualizador en tu máquina local:

```bash
git clone https://github.com/TuUsuario/eft-node.git
cd eft-node
npm install
npm run dev
```
Abre `http://localhost:3000` en tu navegador.

### 2. Actualizar la base de datos por defecto (Solo Admins)
Para mantener el archivo de carga instantánea actualizado después de un wipe masivo, el proyecto incluye un script en Python que extrae los datos de la API y sobrescribe el mapa base.

```bash
# Requiere tener Python instalado
pip install -r requirements.txt
python scripts/update_default_tasks.py
```

## 🤝 Contribuir
EFT.node es un proyecto abierto. Si quieres mejorar la interfaz, añadir nuevos filtros de búsqueda (por comerciantes, mapas, etc.) o corregir algún bug, siéntete libre de abrir un *Issue* o enviar un *Pull Request*.
