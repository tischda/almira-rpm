@echo off
%WINDIR%\system32\tree.com /a /f "e:\software\software-free\almira-dist\almira.dist.rpm" | find /v ".url" | find /v ".txt"

:: Pause with timeout
:: PING 1.1.1.1 -n 1 -w 10000 >NUL
pause

REM TODO: remove also .txt and .md files from the list

