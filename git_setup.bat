@echo off
echo ================================================
echo   DjangoLearn - Git Setup Script (Windows)
echo ================================================
echo.

set /p GITHUB_USERNAME="Enter your GitHub username: "
set /p REPO_NAME="Enter repository name (default: djangolearn): "

if "%REPO_NAME%"=="" set REPO_NAME=djangolearn

echo.
echo Initializing git repository...
git init

echo Creating .gitignore...
echo Already exists in project.

echo.
echo Staging all files...
git add .

echo.
echo Creating initial commit...
git commit -m "Initial commit: DjangoLearn A-Z Tutorial Platform"

echo.
echo Connecting to GitHub...
git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git

echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ================================================
echo   SUCCESS! Code pushed to GitHub.
echo   https://github.com/%GITHUB_USERNAME%/%REPO_NAME%
echo ================================================
pause
