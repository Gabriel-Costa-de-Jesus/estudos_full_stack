@echo off
for /L %%i in (1,1,20) do (
    setlocal enabledelayedexpansion
    set "num=0%%i"
    set "num=!num:~-2!"
    ren "exercise_!num!.por" "exercise_!num!.txt"
    endlocal
)
echo Conversão concluída!
pause
