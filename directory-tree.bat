@echo off
%WINDIR%\system32\tree.com /a /f dist | find /v "download.url"

:: Pause with timeout
:: PING 1.1.1.1 -n 1 -w 10000 >NUL
pause