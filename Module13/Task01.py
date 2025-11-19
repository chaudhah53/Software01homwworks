from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>')
def check_prime(number):
    prime_status = is_prime(number)
    response = {
        "Number": number,
        "isPrime": prime_status
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
