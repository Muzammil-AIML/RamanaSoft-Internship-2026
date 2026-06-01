from fpip lask import Flask, request, render_template_string, redirect

app = Flask(__name__)

@app.route('/')
def ram():
    return redirect('/calculator')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    if request.method == 'POST':
        try:
            a = float(request.form.get('a', 0))
            b = float(request.form.get('b', 0))
            op = request.form.get('operation')
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            else:
                error = 'Invalid operation'
        except Exception:
            error = 'Invalid input'

    return render_template_string('''
        <form method="post">
            <input name="a" placeholder="First number" required>
            <input name="b" placeholder="Second number" required>
            <select name="operation">
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}<p>Result: {{ result }}</p>{% endif %}
        {% if error %}<p>{{ error }}</p>{% endif %}
    ''', result=result, error=error)






if __name__ == '__main__':
    app.run(debug=True, port=5000)