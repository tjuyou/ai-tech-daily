# Horizon 每日自动化 - 右键"使用PowerShell运行"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

# 从系统环境变量读取（或手动设置）
if (-not $env:DEEPSEEK_API_KEY) {
    $env:DEEPSEEK_API_KEY = [Environment]::GetEnvironmentVariable("DEEPSEEK_API_KEY", "User")
}
if (-not $env:DEEPSEEK_API_KEY) {
    Write-Host "ERROR: 请先设置环境变量 DEEPSEEK_API_KEY" -ForegroundColor Red
    Write-Host "  运行: [Environment]::SetEnvironmentVariable('DEEPSEEK_API_KEY', '你的Key', 'User')" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI科技快讯日报 - $(Get-Date -Format 'yyyy-MM-dd HH:mm')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Host "`n[1/4] 抓取国内微博/知乎/百度/抖音热搜..." -ForegroundColor Yellow
uv run python scripts/china_hot_fetcher.py 2>&1

Write-Host "`n[2/4] 运行 Horizon AI日报..." -ForegroundColor Yellow
Copy-Item -Force data/config.github.json data/config.json
uv run horizon --hours 48 2>&1

Write-Host "`n[3/4] DeepSeek改写抖音脚本..." -ForegroundColor Yellow
uv run python scripts/douyin_rewriter.py 2>&1

Write-Host "`n[4/4] 推送到 GitHub Pages..." -ForegroundColor Yellow
git add docs/ -A 2>$null
$date = Get-Date -Format "yyyy-MM-dd"
git commit -m "Daily: $date" 2>$null
git push myrepo main 2>$null

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  Done! https://tjuyou.github.io/ai-tech-daily/" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
