cd "C:\Windows\prefetch"
del . /F /Q

@echo off
del "%tmp%\*.*" /s /q /f
FOR /d %%p IN ("%tmp%\*.*") DO rmdir "%%p" /s /q