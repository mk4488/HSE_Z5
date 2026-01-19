
# Считаем среднее из последовательности Фибоначчи

def fibonacci(n):
    """Генерирует последовательность Фибоначчи"""
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

def calculate(numbers):
    """Вычисляем среднее арифметическое"""
    if not numbers:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    print("вычисляем среднее из 7 чисел Фибоначчи")
    print("=" * 50)
    
    # 7 чисел Фибоначчи
    fib_numbers = fibonacci(7)
    
    # Среднее
    average = calculate(fib_numbers)
    
    # Результаты
    print(f"Последовательность Фибоначчи: {fib_numbers}, среднее арифметическое: {average:.2f}")

if __name__ == "__main__":
    main()