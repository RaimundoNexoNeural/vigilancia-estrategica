@echo off
setlocal
title Visor del corpus - Vigilancia Estrategica Aumentada con IA
cd /d "%~dp0"

set "PUERTO=8080"
if not "%~1"=="" set "PUERTO=%~1"

rem Buscamos Python. No hace falta instalar ninguna libreria: el servidor
rem viene incluido. Probamos a ejecutarlo, no solo a encontrarlo, porque en
rem Windows puede haber un "python" que en realidad abre la Tienda.
set "PY="
python -c "import sys" >nul 2>nul
if %errorlevel% equ 0 set "PY=python"
if defined PY goto tengo
py -c "import sys" >nul 2>nul
if %errorlevel% equ 0 set "PY=py"
if defined PY goto tengo
goto sinpython

:tengo
echo.
echo   Visor del corpus
echo   ----------------
echo   Abriendo http://127.0.0.1:%PUERTO%/
echo.
echo   DEJE ESTA VENTANA ABIERTA mientras use el visor.
echo   Para cerrarlo, cierre esta ventana.
echo.
start "" "http://127.0.0.1:%PUERTO%/"
%PY% -m http.server %PUERTO%
goto fin

:sinpython
echo.
echo   No he encontrado Python en este equipo.
echo.
echo   No pasa nada: no hace falta. El visor esta publicado en internet,
echo   funciona igual y no requiere instalar absolutamente nada:
echo.
echo       https://raimundonexoneural.github.io/vigilancia-estrategica/
echo.
echo   Si aun asi lo quiere en local, Python se descarga en python.org.
echo   Puede que necesite permisos de su departamento de informatica.
echo.
echo   Y en cualquier caso: las noticias de corpus\noticias son ficheros
echo   de texto y los datos de corpus\datos son CSV. Se abren con doble
echo   clic, sin Python y sin visor.
echo.
pause

:fin
endlocal
