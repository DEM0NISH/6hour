# Python setup

The clock simulator uses only Python's standard library; there are no third-party packages to install. Python 3.9 or newer is required.

## Windows PowerShell

From the repository root, run:

```powershell
powershell -ExecutionPolicy Bypass -File tools/setup.ps1
```

This creates `.venv`, checks the simulator's unit tests, and leaves the environment ready to use. Activate it in the current PowerShell session with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then calculate deadlines:

```powershell
python tools/clock_simulator.py --noticed "2026-11-07 02:40" --contract-hours 24
```

Run the unit tests again with:

```powershell
python -m unittest discover -s tools -p "test_*.py"
```

The `.venv` directory is ignored by Git and should not be uploaded; each user can recreate it locally.
