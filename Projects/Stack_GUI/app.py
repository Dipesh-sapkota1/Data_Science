from flask import Flask, render_template, request, jsonify 

app = Flask(__name__)

# Your original Stack class implementation
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            return False, "Stack overflow! Cannot add more items."
        else:
            self.top += 1
            self.stack[self.top] = item
            return True, f"New item is added in the stack: {item}"

    def pop(self):
        if self.top == -1:
            return False, "Stack underflow! No items to remove.", None
        else:
            removed = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return True, f"Item that was removed is: {removed}", removed

    def peek(self):
        if self.top == -1:
            return False, "Stack underflow! No items to peek.", None
        else:
            return True, f"Top item of stack is: {self.stack[self.top]}", self.stack[self.top]

    def display(self):
        if self.top == -1:
            return []
        else:
            # Return items from top to bottom for display
            return [self.stack[i] for i in range(self.top, -1, -1)]
    
    def get_current_items(self):
        """Get all non-None items in the stack"""
        return [self.stack[i] for i in range(self.top + 1)]
    
    def is_full(self):
        """Check if stack is full"""
        return self.top == self.size - 1
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top == -1
    
    def current_size(self):
        """Get current number of items"""
        return self.top + 1
    
    def get_capacity(self):
        """Get maximum capacity"""
        return self.size

# Global stack instance - will be initialized when size is set
stack = None

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/initialize', methods=['POST'])
def initialize_stack():
    """Initialize stack with given size"""
    global stack
    try:
        data = request.get_json()
        size = int(data.get('size', 10))
        
        if size <= 0:
            return jsonify({'error': 'Stack size must be greater than 0'}), 400
        
        if size > 100:
            return jsonify({'error': 'Stack size cannot exceed 100'}), 400
        
        stack = Stack(size)
        return jsonify({
            'success': True,
            'message': f'Stack initialized with size {size}',
            'capacity': stack.get_capacity(),
            'currentSize': stack.current_size(),
            'stack': []
        })
    except ValueError:
        return jsonify({'error': 'Invalid size value'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/push', methods=['POST'])
def push_item():
    """API endpoint to push an item onto the stack"""
    global stack
    if stack is None:
        return jsonify({'error': 'Stack not initialized. Please set stack size first.'}), 400
    
    try:
        data = request.get_json()
        item = data.get('item', '').strip()
        
        if not item:
            return jsonify({'error': 'Item cannot be empty'}), 400
        
        # Try to convert to integer if it's a number
        try:
            if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                item = int(item)
        except:
            pass  # Keep as string if conversion fails
        
        success, message = stack.push(item)
        
        if success:
            return jsonify({
                'success': True,
                'message': message,
                'stack': stack.display(),
                'currentSize': stack.current_size(),
                'capacity': stack.get_capacity(),
                'isFull': stack.is_full()
            })
        else:
            return jsonify({'error': message}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pop', methods=['POST'])
def pop_item():
    """API endpoint to pop an item from the stack"""
    global stack
    if stack is None:
        return jsonify({'error': 'Stack not initialized. Please set stack size first.'}), 400
    
    try:
        success, message, popped_item = stack.pop()
        
        if success:
            return jsonify({
                'success': True,
                'message': message,
                'poppedItem': popped_item,
                'stack': stack.display(),
                'currentSize': stack.current_size(),
                'capacity': stack.get_capacity(),
                'isEmpty': stack.is_empty()
            })
        else:
            return jsonify({'error': message}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/peek', methods=['GET'])
def peek_item():
    """API endpoint to peek at the top item"""
    global stack
    if stack is None:
        return jsonify({'error': 'Stack not initialized. Please set stack size first.'}), 400
    
    try:
        success, message, top_item = stack.peek()
        
        if success:
            return jsonify({
                'success': True,
                'message': message,
                'topItem': top_item,
                'currentSize': stack.current_size()
            })
        else:
            return jsonify({'error': message}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/display', methods=['GET'])
def display_stack():
    """API endpoint to display current stack"""
    global stack
    if stack is None:
        return jsonify({'error': 'Stack not initialized. Please set stack size first.'}), 400
    
    try:
        return jsonify({
            'success': True,
            'stack': stack.display(),
            'currentSize': stack.current_size(),
            'capacity': stack.get_capacity(),
            'isEmpty': stack.is_empty(),
            'isFull': stack.is_full()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """API endpoint to get current stack status"""
    global stack
    if stack is None:
        return jsonify({
            'initialized': False,
            'stack': [],
            'currentSize': 0,
            'capacity': 0,
            'isEmpty': True,
            'isFull': False
        })
    
    return jsonify({
        'initialized': True,
        'stack': stack.display(),
        'currentSize': stack.current_size(),
        'capacity': stack.get_capacity(),
        'isEmpty': stack.is_empty(),
        'isFull': stack.is_full()
    })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)