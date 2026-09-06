# The Code Company — Sitio web corporativo

Sitio web institucional de **The Code Company**, una consultora de desarrollo de software ficticia, construido con **Django 4.2**. Proyecto desarrollado para el curso de Frameworks de Desarrollo Web (Ingeniería de Software, Universidad Autónoma de Zacatecas).

El sitio no es una plantilla estática: cada sección se administra desde el panel de Django, incluyendo un módulo de preguntas y comentarios con **moderación previa**.

---

## Módulos

El proyecto se divide en apps de Django con responsabilidades acotadas:

| App | Modelos | Qué hace |
|---|---|---|
| `tcc` | — | App principal: página de inicio, plantilla base y navegación del sitio. |
| `personal` | `Persona` | Perfiles del equipo: foto (con **validador de imagen personalizado**), habilidades, certificaciones, idiomas, pasatiempos y redes sociales. |
| `clientes` | `cliente` | Cartera de clientes con logotipo, renderizada como carrusel en la portada. |
| `contacto` | `Pregunta`, `Comentario` | Sección de preguntas frecuentes con hilo de comentarios. Los comentarios traen un campo `active` que exige **aprobación desde el admin antes de publicarse**, evitando spam. Las preguntas usan `SlugField` para URLs legibles. |
| `servicios` | — | Catálogo de servicios ofrecidos. |
| `acerca` | — | Página institucional "Acerca de". |

---

## Detalles técnicos

- **Validación de imágenes** — validador propio aplicado al `ImageField` de `Persona`, que restringe formato y tamaño de las fotos subidas.
- **Comentarios moderados** — relación `Pregunta` → `Comentario` con `related_name='comentario'` y bandera `active` por defecto en `False`.
- **Gestión de medios** — carga de archivos a `media/` (logotipos de clientes e imágenes del personal) servidos vía `MEDIA_URL`.
- **Frontend** — plantillas Django sobre una base de **SCSS/LESS** compilada, con assets propios en `static/`.
- **Contenedores** — `Dockerfile` y `docker-compose.yml` que levantan Django junto a **MariaDB**.

---

## Estructura del repositorio

```
.
├── thecodecompany/        # Configuración del proyecto (settings, urls, wsgi)
├── tcc/                   # App principal: home y plantilla base
├── personal/              # Perfiles del equipo (+ validador de imagen)
├── clientes/              # Cartera de clientes
├── contacto/              # Preguntas y comentarios moderados
├── servicios/             # Catálogo de servicios
├── acerca/                # Página institucional
├── static/                # SCSS, LESS, JS, CSS e imágenes
├── media/                 # Archivos subidos por el administrador
├── manage.py
├── Dockerfile
├── docker-compose.yml     # Django + MariaDB
└── requirements.txt
```

---

## Cómo ejecutarlo

### Con Docker

```bash
docker compose up --build
```

El sitio queda disponible en `http://localhost:8000` y MariaDB en el puerto `3310`.

> Las credenciales del `docker-compose.yml` son valores de desarrollo local. Para un despliegue real, muévelas a variables de entorno.

### Sin Docker

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Después entra a `http://localhost:8000/admin` para cargar servicios, clientes, personal y aprobar comentarios.

---

## Stack

`Python 3` · `Django 4.2` · `MariaDB / MySQL` · `Pillow` · `SCSS` · `LESS` · `Docker` · `Docker Compose`

---

## Autor

**Adalberto Cerrillo Vázquez** — Ingeniería de Software, Universidad Autónoma de Zacatecas.
