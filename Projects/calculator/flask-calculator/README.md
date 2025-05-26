# Professional Flask Calculator 🧮

A modern, responsive calculator built with Flask, featuring both light and dark themes.

## Features

- ➕ Basic arithmetic operations
- 🔢 Scientific functions (log, exp, π, factorial, square root)
- 🎨 Light/Dark theme toggle
- ⌨️ Keyboard support
- 📱 Responsive design
- 🎯 Professional file structure

## Setup

### Quick Start
```bash
# Make the setup script executable and run it
chmod +x setup_calculator.sh
./setup_calculator.sh
```

### Manual Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Usage

1. Visit `http://localhost:5000`
2. Use the theme toggle (top-right) to switch between light/dark modes
3. Calculator supports both mouse clicks and keyboard input

### Keyboard Shortcuts
- `0-9, .` : Input numbers and decimal
- `+, -, *, /` : Basic operations
- `Enter` or `=` : Calculate result
- `Escape` or `C` : Clear calculator
- `Backspace` : Delete last digit

## Project Structure

```
flask-calculator/
├── app.py                 # Main application entry point
├── app/
│   ├── __init__.py       # Flask app factory
│   ├── routes.py         # API routes and logic
│   ├── static/
│   │   ├── css/
│   │   │   └── calculator.css
│   │   └── js/
│   │       └── calculator.js
│   └── templates/
│       └── calculator.html
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── .gitignore           # Git ignore patterns
└── README.md            # This file
```

## API Endpoints

- `GET /` - Main calculator interface
- `POST /api/calculate` - Calculator operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use this project for learning or commercial purposes.
