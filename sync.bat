@echo off
cd /d "%~dp0"

set MSG=sync: %date% %time:~0,5%
if not "%~1"=="" set MSG=%~1

git add -A
git commit -m "%MSG%" || echo Nada nuevo que commitear.
git push origin master:main && echo. && echo Push completado. || echo Error en el push.
pause
