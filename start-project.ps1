# Check if Python is installed
Write-Host "Checking if Python is installed..."
if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python 3.11 or higher." -ForegroundColor Red
    exit 1
}

# Check if Node.js is installed
Write-Host "Checking if Node.js is installed..."
if (-Not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "Node.js is not installed. Please install Node.js." -ForegroundColor Red
    exit 1
}

# Check if pip is installed
Write-Host "Checking if pip is installed..."
if (-Not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "pip is not installed. Please install pip." -ForegroundColor Red
    exit 1
}

# Start the backend
Write-Host "Setting up the Python backend..."
Push-Location -Path "./backend"

# Check and install Python dependencies
Write-Host "Installing Python dependencies..."
pip install -r requirements.txt

Push-Location -Path "./fastApiProject"

# Run the FastAPI server
Write-Host "Starting the FastAPI backend on 127.0.0.1:8000..."
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "-m uvicorn main:app --host 127.0.0.1 --port 8000"

Pop-Location
Pop-Location

# Start the frontend
Write-Host "Setting up the Node.js frontend..."
Push-Location -Path "./frontend"

# Check and install Node.js dependencies
Write-Host "Installing Node.js dependencies..."
if (-Not (Test-Path -Path "./node_modules")) {
    npm install
} else {
    Write-Host "Dependencies already installed. Skipping npm install..."
}

# Run the Svelte development server
Write-Host "Starting the Svelte frontend on http://localhost:5173..."
Start-Process -NoNewWindow -FilePath "npm" -ArgumentList "run dev"

Pop-Location

Write-Host "Project setup complete. Backend running on http://127.0.0.1:8000 and frontend on http://localhost:5173."