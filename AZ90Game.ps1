# Check if Python is installed
$pythonInstalled = $null
try {
    $pythonInstalled = python -c "import platform; print(platform.python_version())"
} catch {
    Write-Host "Python is not installed. Please install Python 3 before continuing."
    Exit
}

# Check if the Python version is 3.x
if (-not $pythonInstalled.StartsWith("3")) {
    Write-Host "Python 3 is required. Please install Python 3 before continuing."
    Exit
}

# Check if pandas is installed
$pandasInstalled = $null
try {
    $pandasInstalled = python -c "import pandas; print(pandas.__version__)"
} catch {
    Write-Host "pandas is not installed. Installing pandas..."
    pip install pandas
}

# Start the Python script
Write-Host "Starting AZ900Game.py..."
python AZ900Game.py
