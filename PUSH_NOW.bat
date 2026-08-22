@echo off
echo ============================================
echo PUSHING PRANATHI BRANCH TO GITHUB
echo ============================================
echo.
echo Clearing old GitHub credentials...
cmdkey /list | findstr "github" >nul 2>&1
if %errorlevel%==0 (
    for /f "tokens=2 delims=:" %%a in ('cmdkey /list ^| findstr "github"') do (
        cmdkey /delete:%%a 2>nul
    )
)
echo.
echo Old credentials cleared!
echo.
echo Now attempting to push...
echo Git will ask for your GitHub username and password/token
echo.
pause
echo.
git push -u origin pranathi
echo.
if %errorlevel%==0 (
    echo ============================================
    echo SUCCESS! Code pushed to pranathi branch!
    echo ============================================
) else (
    echo ============================================
    echo FAILED! Please use GitHub Desktop instead
    echo ============================================
)
echo.
pause
