# Horizon 环境安装脚本（只需运行一次）
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Horizon 环境安装" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# 1. 安装 uv（如果还没有）
Write-Host "`n[1/3] 安装 uv..." -ForegroundColor Yellow
$uvInstalled = Get-Command uv -ErrorAction SilentlyContinue
if (-not $uvInstalled) {
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
    Write-Host "  uv 安装完成" -ForegroundColor Green
} else {
    Write-Host "  uv 已安装" -ForegroundColor Green
}

# 2. 安装 Horizon 依赖
Write-Host "`n[2/3] 安装 Horizon 依赖..." -ForegroundColor Yellow
uv sync
Write-Host "  Horizon 依赖安装完成" -ForegroundColor Green

# 3. 安装额外依赖
Write-Host "`n[3/3] 安装额外依赖..." -ForegroundColor Yellow
uv pip install openai
Write-Host "  openai 安装完成" -ForegroundColor Green

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  安装完成！现在可以运行 run_daily.ps1" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
