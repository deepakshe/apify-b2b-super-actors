@echo off
REM =========================================================================
REM  24/7 B2B Marketing & Cold Outbound Autonomous Daemon Launcher
REM  Executes recurring audits every 3 hours across 180+ top B2B companies ($0.00 spend)
REM  Scalable database: master_target_companies.csv (expandable to thousands)
REM =========================================================================

echo Starting 24/7 Autonomous B2B Marketing Daemon...
cd /d "%~dp0..\..\.."

call ".venv\Scripts\activate.bat"
python sales_psychology\distribution_ready_kit\scripts\autonomous_marketing_daemon.py --daemon --interval-hours 3.0 --batch-size 5

pause
