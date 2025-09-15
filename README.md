# Pruebas Automatizadas (Barterflip CMS)

## Objetivo
Automatizar verificaciones críticas de acceso e interfaz para el CMS de Barterflip con **PyTest + Selenium**, facilitando ejecuciones locales y en CI.

## Alcance actual
- **Login exitoso** con credenciales provistas y verificación de llegada al Dashboard.
- **Verificación rápida de Perfil** (opcional) tras el login.
- La suite es extensible a Dashboard, Customer management y Barter Bucks management.

## Estructura sugerida
```
/tests
  └─ test_barterflip_login.py      # Flujo de inicio de sesión + check de perfil
```

> El archivo principal generado es `test_barterflip_login.py`. Puedes moverlo a `/tests` si prefieres esa convención.

## Requisitos
- Python 3.9+
- Google Chrome o Chromium instalado
- Paquetes:
  - selenium
  - webdriver-manager
  - pytest
  - (opcional) pytest-html

Instalación rápida:
```bash
pip install -U selenium webdriver-manager pytest pytest-html
```

## Configuración
Credenciales mediante variables de entorno (recomendado) o valores por defecto en el script.
- `BARTERFLIP_EMAIL` — correo del usuario (elproporcionado)
- `BARTERFLIP_PASSWORD` — contraseña del usuario (el proporcionado)
- `SEL_TIMEOUT` — timeout en segundos para esperas explícitas (por defecto: 20)

## Ejecución
Desde la carpeta donde está el archivo:
```bash
pytest -q test_barterflip_login.py
```
Con variables de entorno:
```bash
BARTERFLIP_EMAIL="tu_correo" BARTERFLIP_PASSWORD="tu_pass" pytest -q test_barterflip_login.py
```

## Notas técnicas
- **Selectores**: se usan localizadores alternativos (CSS/XPath) para tolerar cambios menores.
- **Sincronización**: se emplea `WebDriverWait` con condiciones explícitas.
- **Robustez**: se validan elementos característicos del Dashboard tras el login.
- **Datos**: evita persistir credenciales en el repositorio (usa variables de entorno o un `.env` fuera del control de versiones).

