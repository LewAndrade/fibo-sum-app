from flask import Flask, render_template

app = Flask(__name__)
cache = {}


def fib_sum(number: int):
    """
    Recursively calculates the fibonacci sequence's sum up to a given number.

    :param number: An integer that represents the last fibonacci number.
    :return: The sum of the sequence.
    """

    def _fib_sum(n: int):
        if n < 2:
            cache[n] = n
            return cache[n]
        cache[n] = _fib_sum(n - 1) + _fib_sum(n - 2) + 1
        return cache[n]

    if number not in cache.keys():
        _fib_sum(number)
    return cache[number]


@app.route('/')
def show_main():
    return render_template("main.html")


@app.route('/<number>')
def show_fibonacci(number):
    try:
        return render_template("fibonacci.html", fibo=fib_sum(int(number)))
    except ValueError:
        return "Please use a valid integer as <number>"
    except Exception as e:
        return "Unexpected error: ", type(e), format(e)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
