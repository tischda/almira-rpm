@echo off
call mvn clean assembly:single

:: Pause with timeout
PING 1.1.1.1 -n 1 -w 10000 >NUL
