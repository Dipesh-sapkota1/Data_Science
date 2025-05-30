        class StackGUI {
            constructor() {
                this.messageElement = document.getElementById('message');
                this.stackContainer = document.getElementById('stackContainer');
                this.currentSizeElement = document.getElementById('currentSize');
                this.capacityElement = document.getElementById('capacity');
                this.availableSpaceElement = document.getElementById('availableSpace');
                this.stackStatusElement = document.getElementById('stackStatus');
                this.capacityIndicatorElement = document.getElementById('capacityIndicator');
                this.arrayVisualizationElement = document.getElementById('arrayVisualization');
                this.topPointerElement = document.getElementById('topPointer');
                this.itemInput = document.getElementById('itemInput');
                this.stackSizeInput = document.getElementById('stackSize');
                
                this.isInitialized = false;
                this.updateDisplay();
                
                // Add enter key support
                this.itemInput.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter' && this.isInitialized) {
                        this.pushItem();
                    }
                });

                this.stackSizeInput.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') {
                        this.initializeStack();
                    }
                });
            }

            async makeRequest(url, options = {}) {
                try {
                    const response = await fetch(url, {
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        ...options
                    });
                    return await response.json();
                } catch (error) {
                    this.showMessage('Network error occurred', 'error');
                    console.error('Request failed:', error);
                    return null;
                }
            }

            async initializeStack() {
                const size = parseInt(this.stackSizeInput.value);
                if (!size || size < 1 || size > 100) {
                    this.showMessage('Please enter a valid size between 1 and 100', 'error');
                    return;
                }

                const result = await this.makeRequest('/api/initialize', {
                    method: 'POST',
                    body: JSON.stringify({ size: size })
                });

                if (result && result.success) {
                    this.isInitialized = true;
                    this.showMessage(result.message, 'success');
                    this.updateDisplay(result);
                    this.enableControls();
                    this.itemInput.focus();
                } else if (result) {
                    this.showMessage(result.error, 'error');
                }
            }

            async pushItem() {
                if (!this.isInitialized) return;

                const item = this.itemInput.value.trim();
                if (!item) {
                    this.showMessage('Please enter an item to push', 'error');
                    return;
                }

                const result = await this.makeRequest('/api/push', {
                    method: 'POST',
                    body: JSON.stringify({ item: item })
                });

                if (result) {
                    if (result.success) {
                        this.showMessage(result.message, 'success');
                        this.updateDisplay(result);
                        this.itemInput.value = '';
                        this.itemInput.focus();
                    } else {
                        this.showMessage(result.error, 'error');
                    }
                }
            }

            async popItem() {
                if (!this.isInitialized) return;

                const result = await this.makeRequest('/api/pop', {
                    method: 'POST'
                });

                if (result) {
                    if (result.success) {
                        this.showMessage(result.message, 'success');
                        this.updateDisplay(result);
                    } else {
                        this.showMessage(result.error, 'error');
                    }
                }
            }

            async peekItem() {
                if (!this.isInitialized) return;

                const result = await this.makeRequest('/api/peek');

                if (result) {
                    if (result.success) {
                        this.showMessage(result.message, 'info');
                    } else {
                        this.showMessage(result.error, 'error');
                    }
                }
            }

            async displayStack() {
                if (!this.isInitialized) return;

                const result = await this.makeRequest('/api/display');

                if (result) {
                    if (result.success) {
                        this.updateDisplay(result);
                        this.showMessage('Stack display refreshed', 'info');
                    } else {
                        this.showMessage(result.error, 'error');
                    }
                }
            }

                        updateDisplay(data = null) {
                            if (!this.isInitialized || !data) {
                                this.updateInitialState();
                                return;
                            }
            
                            // Update info card
                            this.currentSizeElement.textContent = data.currentSize || 0;
                            this.capacityElement.textContent = data.capacity || 0;
                            this.availableSpaceElement.textContent = (data.capacity || 0) - (data.currentSize || 0);
            
                            // Update status
                            let status = 'Initialized';
                            let statusClass = 'status-partial';
                            
                            if (data.isEmpty) {
                                status = 'Empty';
                                statusClass = 'status-empty';
                            } else if (data.isFull) {
                                status = 'Full';
                                statusClass = 'status-full';
                            }
            
                            this.stackStatusElement.innerHTML = `${status} <span class="status-indicator ${statusClass}"></span>`;
            
                            // Update capacity indicator
                            this.capacityIndicatorElement.textContent = `Capacity: ${data.capacity || 0}`;
                            
                            // Update array visualization
                            this.renderArrayVisualization(data);
            
                            // Update stack contents
                            this.renderStackContents(data);
            
                            // Update top pointer
                            this.topPointerElement.textContent = `TOP = ${typeof data.top === 'number' ? data.top : -1}`;
                        }
            
                        updateInitialState() {
                            this.currentSizeElement.textContent = '0';
                            this.capacityElement.textContent = '0';
                            this.availableSpaceElement.textContent = '0';
                            this.stackStatusElement.innerHTML = `Not Initialized <span class="status-indicator status-empty"></span>`;
                            this.capacityIndicatorElement.textContent = 'Not Initialized';
                            this.arrayVisualizationElement.innerHTML = `<div style="text-align: center; color: #999; padding: 20px;">
                                        Initialize stack to see array visualization
                                    </div>`;
                            this.topPointerElement.textContent = 'TOP = -1';
                            this.stackContainer.innerHTML = `<div class="stack-empty">
                                        Stack not initialized<br>
                                        <small>Initialize the stack to get started!</small>
                                    </div>`;
                            this.disableControls();
                        }
            
                        renderArrayVisualization(data) {
                            if (!data || !Array.isArray(data.array)) {
                                this.arrayVisualizationElement.innerHTML = `<div style="text-align: center; color: #999; padding: 20px;">
                                        Initialize stack to see array visualization
                                    </div>`;
                                return;
                            }
                            let html = '';
                            data.array.forEach((item, idx) => {
                                let classes = 'array-slot';
                                if (idx <= data.top) classes += ' filled';
                                if (idx === data.top) classes += ' top';
                                html += `<div class="${classes}">
                                            ${item !== null && idx <= data.top ? item : ''}
                                            <span class="index">${idx}</span>
                                        </div>`;
                            });
                            this.arrayVisualizationElement.innerHTML = html;
                        }
            
                        renderStackContents(data) {
                            if (!data || !Array.isArray(data.stack) || data.stack.length === 0) {
                                this.stackContainer.innerHTML = `<div class="stack-empty">
                                        Stack is empty<br>
                                        <small>Push items to see them here!</small>
                                    </div>`;
                                return;
                            }
                            let html = '';
                            data.stack.forEach((item, idx) => {
                                html += `<div class="stack-item">${item}</div>`;
                            });
                            this.stackContainer.innerHTML = html;
                        }
            
                        showMessage(msg, type = 'info') {
                            this.messageElement.textContent = msg;
                            this.messageElement.className = `message ${type}`;
                            this.messageElement.style.display = 'block';
                            clearTimeout(this._msgTimeout);
                            this._msgTimeout = setTimeout(() => {
                                this.messageElement.style.display = 'none';
                            }, 3000);
                        }
            
                        enableControls() {
                            document.querySelectorAll('.btn').forEach(btn => btn.disabled = false);
                            this.itemInput.disabled = false;
                        }
            
                        disableControls() {
                            document.querySelectorAll('.btn').forEach(btn => btn.disabled = true);
                            this.itemInput.disabled = true;
                        }
                    }
            
                    // Instantiate and wire up the GUI
                    const stackGUI = new StackGUI();
            
                    // Expose functions for button onclick handlers
                    function initializeStack() { stackGUI.initializeStack(); }
                    function pushItem() { stackGUI.pushItem(); }
                    function popItem() { stackGUI.popItem(); }
                    function peekItem() { stackGUI.peekItem(); }
                    function displayStack() { stackGUI.displayStack(); }
              