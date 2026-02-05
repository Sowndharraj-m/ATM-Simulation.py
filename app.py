from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'atm_secret_key_2024'

# Default account settings
DEFAULT_PIN = "1234"
DEFAULT_BALANCE = 5000.0
MAX_ATTEMPTS = 3


def init_session():
    """Initialize session with default values if not set"""
    if 'pin' not in session:
        session['pin'] = DEFAULT_PIN
    if 'balance' not in session:
        session['balance'] = DEFAULT_BALANCE
    if 'attempts' not in session:
        session['attempts'] = MAX_ATTEMPTS
    if 'logged_in' not in session:
        session['logged_in'] = False
    if 'blocked' not in session:
        session['blocked'] = False


@app.route('/')
def login():
    """Login page with PIN entry"""
    init_session()
    if session.get('blocked'):
        return render_template('login.html', error="Card blocked. Too many wrong attempts.", blocked=True)
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))
    return render_template('login.html', attempts=session.get('attempts', MAX_ATTEMPTS))


@app.route('/verify-pin', methods=['POST'])
def verify_pin():
    """Verify the entered PIN"""
    init_session()
    
    if session.get('blocked'):
        return jsonify({'success': False, 'error': 'Card blocked', 'blocked': True})
    
    entered_pin = request.json.get('pin', '')
    
    if entered_pin == session['pin']:
        session['logged_in'] = True
        session['attempts'] = MAX_ATTEMPTS
        return jsonify({'success': True})
    else:
        session['attempts'] -= 1
        if session['attempts'] <= 0:
            session['blocked'] = True
            return jsonify({'success': False, 'error': 'Card blocked. Too many wrong attempts.', 'blocked': True})
        return jsonify({'success': False, 'error': f'Wrong PIN. {session["attempts"]} attempts left.', 'attempts': session['attempts']})


@app.route('/dashboard')
def dashboard():
    """Main ATM dashboard"""
    init_session()
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html', balance=session['balance'])


@app.route('/api/balance')
def get_balance():
    """Get current balance"""
    if not session.get('logged_in'):
        return jsonify({'error': 'Not logged in'}), 401
    return jsonify({'balance': session['balance']})


@app.route('/api/deposit', methods=['POST'])
def deposit():
    """Deposit money"""
    if not session.get('logged_in'):
        return jsonify({'error': 'Not logged in'}), 401
    
    try:
        amount = float(request.json.get('amount', 0))
        if amount <= 0:
            return jsonify({'success': False, 'error': 'Amount must be greater than 0'})
        
        session['balance'] += amount
        return jsonify({'success': True, 'balance': session['balance'], 'message': f'Deposited ₹{amount:.2f} successfully!'})
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid amount'})


@app.route('/api/withdraw', methods=['POST'])
def withdraw():
    """Withdraw money"""
    if not session.get('logged_in'):
        return jsonify({'error': 'Not logged in'}), 401
    
    try:
        amount = float(request.json.get('amount', 0))
        if amount <= 0:
            return jsonify({'success': False, 'error': 'Amount must be greater than 0'})
        if amount > session['balance']:
            return jsonify({'success': False, 'error': 'Insufficient balance'})
        
        session['balance'] -= amount
        return jsonify({'success': True, 'balance': session['balance'], 'message': f'Withdrawn ₹{amount:.2f} successfully!'})
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid amount'})


@app.route('/api/change-pin', methods=['POST'])
def change_pin():
    """Change PIN"""
    if not session.get('logged_in'):
        return jsonify({'error': 'Not logged in'}), 401
    
    old_pin = request.json.get('old_pin', '')
    new_pin = request.json.get('new_pin', '')
    
    if old_pin != session['pin']:
        return jsonify({'success': False, 'error': 'Incorrect old PIN'})
    
    if len(new_pin) != 4 or not new_pin.isdigit():
        return jsonify({'success': False, 'error': 'PIN must be exactly 4 digits'})
    
    session['pin'] = new_pin
    return jsonify({'success': True, 'message': 'PIN changed successfully!'})


@app.route('/logout')
def logout():
    """Logout and clear session"""
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/reset')
def reset():
    """Reset entire session (for testing)"""
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
