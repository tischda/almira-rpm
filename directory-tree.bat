@echo off
%WINDIR%\system32\tree.com /a /f dist | find /v ".url"

:: Pause with timeout
:: PING 1.1.1.1 -n 1 -w 10000 >NUL
pause

REM TODO: remove also .txt and .md files from the list

