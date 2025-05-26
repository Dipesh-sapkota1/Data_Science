class Calculator {
    constructor() {
        this.currentInput = '0';
        this.currentExpression = '';
        this.shouldResetDisplay = false;
        this.lastResult = null;
        
        this.initializeTheme();
        this.bindEvents();
        this.updateDisplay();
    }

    initializeTheme() {
        const themeToggle = document.getElementById('theme-toggle');
        const savedTheme = localStorage.getItem('calculator-theme') || 'light';
        
        if (savedTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeToggle.checked = true;
        }

        themeToggle.addEventListener('change', () => {
            const theme = themeToggle.checked ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('calculator-theme', theme);
        });
    }

    bindEvents() {
        // Keyboard support
        document.addEventListener('keydown', (e) => {
            e.preventDefault();
            this.handleKeyboard(e.key);
        });
    }

    handleKeyboard(key) {
        if (/[0-9.]/.test(key)) {
            this.inputNumber(key);
        } else if (['+', '-', '*', '/'].includes(key)) {
            const operators = {'+': '+', '-': '-', '*': '×', '/': '÷'};
            this.inputOperator(operators[key]);
        } else if (key === 'Enter' || key === '=') {
            this.calculate();
        } else if (key === 'Escape' || key.toLowerCase() === 'c') {
            this.clearCalc();
        } else if (key === 'Backspace') {
            this.backspace();
        }
    }

    updateDisplay() {
        const display = document.getElementById('current-display');
        display.textContent = this.formatNumber(this.currentInput);
    }

    formatNumber(num) {
        if (num === 'Error' || num === 'Infinity' || num === '-Infinity') return num;
        
        const number = parseFloat(num);
        if (isNaN(number)) return num;
        
        // Handle very large or very small numbers
        if (Math.abs(number) > 1e10 || (Math.abs(number) < 1e-6 && number !== 0)) {
            return number.toExponential(6);
        }
        
        return number.toLocaleString(undefined, {maximumFractionDigits: 10});
    }

    inputNumber(num) {
        if (this.shouldResetDisplay || this.currentInput === '0') {
            this.currentInput = num === '.' ? '0.' : num;
            this.shouldResetDisplay = false;
        } else {
            if (num === '.' && this.currentInput.includes('.')) return;
            this.currentInput += num;
        }
        this.updateDisplay();
    }

    inputOperator(op) {
        if (this.currentExpression && !this.shouldResetDisplay) {
            this.calculate();
        }
        this.currentExpression = this.currentInput + ' ' + op + ' ';
        document.getElementById('history').textContent = this.currentExpression;
        this.shouldResetDisplay = true;
    }

    clearCalc() {
        this.currentInput = '0';
        this.currentExpression = '';
        document.getElementById('history').textContent = '';
        this.shouldResetDisplay = false;
        this.updateDisplay();
    }

    backspace() {
        if (this.currentInput.length > 1) {
            this.currentInput = this.currentInput.slice(0, -1);
        } else {
            this.currentInput = '0';
        }
        this.updateDisplay();
    }

    async calculate() {
        if (!this.currentExpression) return;
        
        const fullExpression = this.currentExpression + this.currentInput;
        
        try {
            const response = await fetch('/api/calculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ expression: fullExpression, operation: 'equals' })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.lastResult = data.result;
                this.currentInput = data.result;
                this.currentExpression = '';
                document.getElementById('history').textContent = fullExpression + ' =';
                this.shouldResetDisplay = true;
            } else {
                this.currentInput = 'Error';
                this.shouldResetDisplay = true;
            }
            
            this.updateDisplay();
        } catch (error) {
            console.error('Calculation error:', error);
            this.currentInput = 'Error';
            this.shouldResetDisplay = true;
            this.updateDisplay();
        }
    }

    async operation(op) {
        if (this.currentInput === 'Error') {
            this.clearCalc();
            return;
        }

        try {
            const response = await fetch('/api/calculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ expression: this.currentInput, operation: op })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.currentInput = data.result;
                this.shouldResetDisplay = true;
                
                // Update history for special operations
                const opNames = {
                    'log': 'log',
                    'sqrt': '√',
                    'factorial': '!',
                    'exp': 'e^',
                    'pi': 'π',
                    'percent': '%'
                };
                
                if (op !== 'pi') {
                    document.getElementById('history').textContent = 
                        opNames[op] + '(' + (op === 'pi' ? '' : this.lastResult || this.currentInput) + ')';
                }
            } else {
                this.currentInput = 'Error';
                this.shouldResetDisplay = true;
            }
            
            this.updateDisplay();
        } catch (error) {
            console.error('Operation error:', error);
            this.currentInput = 'Error';
            this.shouldResetDisplay = true;
            this.updateDisplay();
        }
    }
}

// Global functions for HTML onclick events
let calc;

function inputNumber(num) { calc.inputNumber(num); }
function inputOperator(op) { calc.inputOperator(op); }
function clearCalc() { calc.clearCalc(); }
function calculate() { calc.calculate(); }
function operation(op) { calc.operation(op); }

// Initialize calculator when page loads
document.addEventListener('DOMContentLoaded', () => {
    calc = new Calculator();
});
