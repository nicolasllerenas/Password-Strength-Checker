# 🔐 Verificador de Fortaleza de Contraseñas

Un proyecto de ciberseguridad que utiliza expresiones regulares (regex) para evaluar la fortaleza de contraseñas. Incluye tanto una interfaz gráfica (GUI) como una interfaz de línea de comandos (CLI).

## 🚀 Características

### Criterios de Evaluación
- **Longitud mínima**: 8 caracteres
- **Mayúsculas**: Al menos una letra mayúscula
- **Minúsculas**: Al menos una letra minúscula
- **Números**: Al menos un dígito
- **Caracteres especiales**: Al menos un carácter especial
- **Sin espacios**: No debe contener espacios
- **Sin patrones comunes**: No debe contener secuencias comunes como "123", "abc", "password", etc.

### Sistema de Puntuación
- **Muy Fuerte**: 7-8 puntos
- **Fuerte**: 5-6 puntos
- **Media**: 3-4 puntos
- **Débil**: 1-2 puntos
- **Muy Débil**: 0 puntos

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Expresiones Regulares (re)**: Para validación de patrones
- **Tkinter**: Para la interfaz gráfica
- **Sistema de puntuación**: Para evaluar la fortaleza

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd Password-Strength-Checker
```

2. Asegúrate de tener Python 3.x instalado:
```bash
python --version
```

3. No se requieren dependencias adicionales (tkinter viene incluido con Python)

## 🎯 Uso

### Interfaz Gráfica (Por defecto)
```bash
python main.py
```

### Interfaz de Línea de Comandos
```bash
python main.py --cli
```

## 📱 Interfaz Gráfica

La GUI incluye:
- Campo de entrada de contraseña (oculta por defecto)
- Opción para mostrar/ocultar la contraseña
- Evaluación en tiempo real
- Puntaje visual (0-8)
- Lista detallada de criterios cumplidos/incumplidos
- Colores indicativos de fortaleza

## 💻 Interfaz de Línea de Comandos

La CLI ofrece:
- Entrada interactiva de contraseñas
- Resultados detallados en consola
- Bucle continuo hasta salir
- Comandos de salida: 'quit', 'exit', 'salir'

## 🔍 Ejemplos de Uso

### Contraseñas de Ejemplo

**Muy Fuerte (8/8 puntos):**
```
MyP@ssw0rd2024!
```

**Fuerte (6/8 puntos):**
```
SecurePass123
```

**Media (4/8 puntos):**
```
mypassword123
```

**Débil (2/8 puntos):**
```
password
```

**Muy Débil (0/8 puntos):**
```
123
```

## 🧪 Expresiones Regulares Utilizadas

```python
# Longitud mínima
r'.{8,}'

# Mayúsculas
r'[A-Z]'

# Minúsculas
r'[a-z]'

# Números
r'\d'

# Caracteres especiales
r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]'

# Sin espacios
r'^\S*$'

# Sin patrones comunes
r'^(?!.*(?:123|abc|qwe|password|admin|user|test|123456|qwerty)).*$'
```

## 🏗️ Estructura del Proyecto

```
Password-Strength-Checker/
├── main.py          # Script principal
└── README.md        # Documentación
```

## 🔧 Clases Principales

### PasswordStrengthChecker
- Clase principal para evaluar contraseñas
- Utiliza regex para validar criterios
- Retorna fortaleza, puntaje y feedback

### PasswordGUI
- Interfaz gráfica con Tkinter
- Evaluación en tiempo real
- Diseño moderno y responsivo

## 🎨 Características de la GUI

- **Diseño moderno**: Colores profesionales y tipografía clara
- **Feedback visual**: Colores indicativos de fortaleza
- **Scroll automático**: Para listas largas de criterios
- **Responsive**: Se adapta al contenido
- **Accesibilidad**: Opción para mostrar/ocultar contraseña

## 🔒 Seguridad

- Las contraseñas no se almacenan
- Evaluación en tiempo real sin persistencia
- Interfaz segura con opción de ocultar contraseña

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👨‍💻 Autor

Proyecto de ciberseguridad para aprendizaje de expresiones regulares y desarrollo de aplicaciones de seguridad.

---

**¡Mejora la seguridad de tus contraseñas con este verificador!** 🔐✨