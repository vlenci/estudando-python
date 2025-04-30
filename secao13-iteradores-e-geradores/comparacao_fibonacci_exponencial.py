def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


def comparar_fib_vs_exp(limite=20):
    print(f"{'n':>2} | {'Fibonacci':>10} | {'2^n':>10} | {'Maior valor':>12}")
    print("-" * 43)
    for n, fib_val in enumerate(fibonacci(limite)):
        exp_val = 2**n
        maior = "Fibonacci" if fib_val > exp_val else "2^n"
        print(f"{n:>2} | {fib_val:>10} | {exp_val:>10} | {maior:>12}")


comparar_fib_vs_exp(100)
