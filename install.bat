@echo off
REM ==============================================================================
REM VJSS: Universal AI Agent Super-Skills Ecosystem Windows CMD Installer
REM Creator & Lead Architect: Mr. Vishalkumar Joshi
REM Email: mrvishaljjoshi@gmail.com | Website: https://vjprojects.co.in
REM GitHub: https://github.com/mrvishaljjoshi-cmyk | Repo: https://github.com/mrvishaljjoshi-cmyk/VJSS
REM ==============================================================================

echo ===============================================================================
echo       VJSS: UNIVERSAL AI AGENT SUPER-SKILLS INSTALLER (Windows)
echo              Creator & Lead Architect: Mr. Vishalkumar Joshi
echo        Website: https://vjprojects.co.in ^| Email: mrvishaljjoshi@gmail.com
echo                    130 Plain-Text Engineering Protocols + JIT Fetch
echo ===============================================================================
echo.
echo Select target tool to install VJSS Bootloader:
echo  1. Claude Code (CLAUDE.md)
echo  2. Cursor IDE (.cursorrules ^& .cursor/rules/)
echo  3. Windsurf IDE (.windsurfrules)
echo  4. VS Code Copilot (.github/copilot-instructions.md)
echo  5. Roo Code ^& Cline (.clinerules ^& .roomodes)
echo  6. Install ALL Tools
echo  7. Exit
echo.
set /p choice="Enter choice [1-6]: "

if "%choice%"=="1" goto install_claude
if "%choice%"=="2" goto install_cursor
if "%choice%"=="3" goto install_windsurf
if "%choice%"=="4" goto install_vscode
if "%choice%"=="5" goto install_cline
if "%choice%"=="6" goto install_all
goto end

:install_claude
powershell -ExecutionPolicy Bypass -File install.ps1 -Tool claude
goto end

:install_cursor
powershell -ExecutionPolicy Bypass -File install.ps1 -Tool cursor
goto end

:install_windsurf
powershell -ExecutionPolicy Bypass -File install.ps1 -Tool windsurf
goto end

:install_vscode
powershell -ExecutionPolicy Bypass -File install.ps1 -Tool vscode
goto end

:install_cline
powershell -ExecutionPolicy Bypass -File install.ps1 -Tool cline
goto end

:install_all
powershell -ExecutionPolicy Bypass -File install.ps1 -Tool all
goto end

:end
echo.
pause
