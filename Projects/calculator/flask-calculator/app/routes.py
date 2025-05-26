from flask import Blueprint, render_template, request, jsonify
import math

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('calculator.html')

@main.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        expression = data.get('expression', '')
        operation = data.get('operation', '')
        
        if operation == 'clear':
            return jsonify({'result': '0', 'success': True})
        
        elif operation == 'equals':
            try:
                # Replace common symbols for evaluation
                expression = expression.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                return jsonify({'result': str(result), 'success': True})
            except:
                return jsonify({'result': 'Error', 'success': False})
        
        elif operation == 'log':
            try:
                num = float(expression) if expression else 0
                if num <= 0:
                    return jsonify({'result': 'Error', 'success': False})
                result = math.log10(num)
                return jsonify({'result': str(result), 'success': True})
            except:
                return jsonify({'result': 'Error', 'success': False})
        
        elif operation == 'exp':
            try:
                num = float(expression) if expression else 0
                result = math.exp(num)
                return jsonify({'result': str(result), 'success': True})
            except:
                return jsonify({'result': 'Error', 'success': False})
        
        elif operation == 'pi':
            return jsonify({'result': str(math.pi), 'success': True})
        
        elif operation == 'factorial':
            try:
                num = int(float(expression)) if expression else 0
                if num < 0:
                    return jsonify({'result': 'Error', 'success': False})
                result = math.factorial(num)
                return jsonify({'result': str(result), 'success': True})
            except:
                return jsonify({'result': 'Error', 'success': False})
        
        elif operation == 'sqrt':
            try:
                num = float(expression) if expression else 0
                if num < 0:
                    return jsonify({'result': 'Error', 'success': False})
                result = math.sqrt(num)
                return jsonify({'result': str(result), 'success': True})
            except:
                return jsonify({'result': 'Error', 'success': False})
        
        elif operation == 'percent':
            try:
                num = float(expression) if expression else 0
                result = num / 100
                return jsonify({'result': str(result), 'success': True})
            except:
                return jsonify({'result': 'Error', 'success': False})
        
        else:
            return jsonify({'result': expression, 'success': True})
            
    except Exception as e:
        return jsonify({'result': 'Error', 'success': False})
