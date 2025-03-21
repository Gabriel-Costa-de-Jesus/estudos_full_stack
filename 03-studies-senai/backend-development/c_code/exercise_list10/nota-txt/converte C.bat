@echo off
for /L %%i in (1,1,20) do (
    ren "main%%i.c" "main%%i.txt"
)
echo Conversão concluída!
pause
