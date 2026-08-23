@echo off
echo ========================================
echo    EASIEST WAY TO PUSH CODE
echo ========================================
echo.
echo I will help you push code to GitHub!
echo.
echo OPTION 1: GitHub Desktop (Easiest - No password needed!)
echo ---------------------------------------------------------
echo 1. Open GitHub Desktop application
echo 2. You'll see "Push origin" button at top
echo 3. Click it
echo 4. Done! That's it!
echo.
echo.
echo OPTION 2: Generate Token and Push (Takes 2 minutes)
echo ---------------------------------------------------------
echo 1. Go to: https://github.com/settings/tokens
echo 2. Click "Generate new token (classic)"
echo 3. Give it a name: "marketplace-push"
echo 4. Check: "repo" (all boxes under it)
echo 5. Click "Generate token"
echo 6. COPY the token (you won't see it again!)
echo 7. Come back here and run this:
echo.
echo    git push https://YOUR_TOKEN_HERE@github.com/charanroyal00/old-currency-marketplace.git pranathi
echo.
echo    (Replace YOUR_TOKEN_HERE with the token you copied)
echo.
echo.
echo OPTION 3: Ask a friend who has access to the repo
echo ---------------------------------------------------------
echo Send them this folder as ZIP
echo They can push for you
echo.
echo.
pause
echo.
echo ========================================
echo Which option did you choose?
echo ========================================
echo.
echo Press 1 for GitHub Desktop
echo Press 2 for Token method
echo Press 3 for Friend help
echo.
choice /c 123 /n /m "Enter your choice (1, 2, or 3): "

if errorlevel 3 goto friend
if errorlevel 2 goto token
if errorlevel 1 goto desktop

:desktop
echo.
echo ========================================
echo OPENING GITHUB DESKTOP...
echo ========================================
echo.
echo If GitHub Desktop doesn't open, open it manually
echo Then click "Push origin" button
echo.
start github-desktop://
timeout /t 3
echo.
echo Did it work?
pause
goto end

:token
echo.
echo ========================================
echo TOKEN METHOD
echo ========================================
echo.
echo Step 1: Open this in browser:
echo https://github.com/settings/tokens
echo.
start https://github.com/settings/tokens
echo.
echo Step 2: Generate token and copy it
echo.
set /p TOKEN="Step 3: Paste your token here and press Enter: "
echo.
echo Pushing to GitHub...
echo.
git push https://%TOKEN%@github.com/charanroyal00/old-currency-marketplace.git pranathi
echo.
if %errorlevel%==0 (
    echo ========================================
    echo SUCCESS! Code pushed to GitHub!
    echo ========================================
    echo.
    echo Now go to Render and click "Manual Deploy"
) else (
    echo ========================================
    echo FAILED! Check if token is correct
    echo ========================================
)
pause
goto end

:friend
echo.
echo ========================================
echo FRIEND HELP METHOD
echo ========================================
echo.
echo 1. Right-click this folder
echo 2. Send to → Compressed (zipped) folder
echo 3. Send ZIP to your friend
echo 4. Friend extracts and runs: git push origin pranathi
echo.
pause
goto end

:end
echo.
echo Thank you!
