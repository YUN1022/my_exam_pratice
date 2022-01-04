from flask import Flask, request

app = Flask(__name__)


@app.get('/greeting')
def hello():
    return 'Hello, World'


@app.get('/fib')
def get_fib():
    n = int(request.args.get('n'))
    if n < 2:
        return {'ans': n}

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return {'ans': dp[-1]}


@app.post('/fib')
def post_fib():
    n = int(request.form.get('n', 0))
    if n < 2:
        return {'ans': n}

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return {'ans': dp[-1]}


@app.put('/fib')
def put_fib():
    n = int(request.form.get('n', 0))
    if n < 2:
        return {'ans': n}

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return {'ans': dp[-1]}


@app.delete('/fib')
def delete_fib():
    n = int(request.form.get('n', 0))
    return {'delete': n}


if __name__ == '__main__':
    app.run(port=5000)
