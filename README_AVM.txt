
Proyecto: AVM NACIMIENTOS – Login con Python y HTML Bootstrap

Descripción:
Este proyecto permite iniciar sesión como administrador o usuario básico y redirige al panel correspondiente. 
Se conecta con una base de datos SQLite.

Requisitos:
- Python 3.10 o superior
- Un navegador web moderno
- No se necesita instalar nada adicional

Contenido del proyecto:
- backend_login.py: servidor que procesa login y entrega páginas HTML
- avm_base.sqlite: base de datos con la tabla 'usuarios' ya cargada
- index.html: formulario de login en Bootstrap
- admin.html / usuario.html: pantallas de inicio según el tipo de usuario
- crear_usuarios.py: script opcional para insertar usuarios si la tabla está vacía

Cómo ejecutar:
1. Abrir terminal en la carpeta del proyecto
2. Ejecutar:
   python backend_login.py
3. Ir al navegador y escribir:
   http://localhost:8000/index.html

Usuarios de prueba:
| Tipo         | Usuario   | Contraseña   |
|--------------|-----------|--------------|
| Administrador| admin     | admin123     |
| Usuario      | usuario   | usuario123   |
