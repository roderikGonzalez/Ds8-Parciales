# Ds8-Parciales

Desarrollo de Software VIII — Parciales 2 y 3.  
**Integrantes:** Roderik González, Luis Alain, Freddy Herrera.

---

# Página web - Hosting de servidor de Minecraft

Desarrollo de una aplicación web con **Streamlit** para gestionar un servidor de Minecraft, utilizando una base de datos en la nube **Supabase** y desplegada automáticamente en **Railway**.  
El proyecto implementa buenas prácticas de desarrollo, integración continua y despliegue continuo (CI/CD) mediante **GitHub Actions** y control de código colaborativo en **GitHub**.

---

## 1. Tecnologías utilizadas

- **Python 3.11**
- **Streamlit** – interfaz web principal  
- **Supabase** – base de datos SQL en la nube  
- **Railway** – plataforma para despliegue (PaaS)  
- **GitHub Actions** – automatización de flujos (lint y deploy)  
- **Ruff** – linter PEP8  
- **python-dotenv** – manejo de variables de entorno

---

## 2. Instalación local

### Clonar el repositorio por HTTPS
```bash
git clone https://github.com/roderikGonzalez/Ds8-Parciales.git

cd Ds8-Parciales

python -m venv venv

```

### Activar entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

---


---

## 4. Ejecución del proyecto localmente
```bash
streamlit run app.py
```

Luego abre el enlace que aparece en la consola (por defecto: [http://localhost:8501](http://localhost:8501)).

---

## 5. Estructura del proyecto

```
Ds8-Parciales/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── workflows/
│   │   ├── ruff.yml
│   │   └── deploy.yml
│   └── PULL_REQUEST_TEMPLATE.md
│
├── complements/
│   ├── 1_Información_del_Servidor.py
│   └── 2_Jugadores_Activos.py
│
├── src/
│   ├── config.py
│   ├── database.py
│   └── utils.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── railway.json
└── app.py
```

---

## 6. Automatizaciones CI/CD

### **Linter (Ruff)**
Workflow: `.github/workflows/ruff.yml`
- Ejecuta Ruff para validar el formato PEP8 en cada push o pull request.

### **Despliegue automático**
Workflow: `.github/workflows/deploy.yml`
- Railway se conecta automáticamente al repositorio.  
- Cada vez que se hace `push` en la rama `main`, GitHub Actions ejecuta el despliegue.

---

## 7. Buenas prácticas aplicadas

- Flujo de trabajo **GitHub Flow**
- **Branch protection** (main protegida)
- **Commits semánticos** (`feat:`, `fix:`, `chore:`, etc.)
- **Pull requests revisadas**
- **Etiquetas de issues** (`bug`, `tarea`, `enhancement`, etc.)
- **Plantillas de PR e Issues**
- **Linter Ruff** y **PEP8**
- **Variables seguras (.env / Railway secrets)**
- **Deploy automatizado** con GitHub Actions

---

## 8. Licencia

Este proyecto se distribuye bajo la licencia **MIT**.  
Consulta el archivo `LICENSE` para más información.
