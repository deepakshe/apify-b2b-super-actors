# =========================================================================
#  24/7 B2B Marketing & Cold Outbound Autonomous Daemon (PowerShell)
#  Runs recurring audits every 3 hours across 180+ top B2B companies ($0.00 spend)
#  Scalable database: master_target_companies.csv (expandable to thousands)
# =========================================================================

$ErrorActionPreference = "Continue"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path "$ScriptDir\..\..\.."

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "   STARTING 24/7 B2B MARKETING & COLD OUTBOUND DAEMON           " -ForegroundColor Green
Write-Host "   Interval: Every 3 Hours | Database: 180+ Accounts | Cost: $0 " -ForegroundColor Yellow
Write-Host "=================================================================" -ForegroundColor Cyan

$PythonExe = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
$DaemonScript = Join-Path $ProjectRoot "sales_psychology\distribution_ready_kit\scripts\autonomous_marketing_daemon.py"

& $PythonExe $DaemonScript --daemon --interval-hours 3.0 --batch-size 5
