УКРАЇНСЬКИЙ КАТОЛИЦЬКИЙ УНІВЕРСИТЕТ
ФАКУЛЬТЕТ ПРИКЛАДНИХ НАУК
ІТ та Бізнес-Аналітикa. 
Розклад функції  2^x/(1-x) в ряд Тейлора та обрахунок наближення за допомогою Python
                                    	          	 	Автор:
                                                             	Богун Максим    
            
20 Лютого 2022
 

1.   Процес розробки.
	Реалізація проєкту проходила в декілька етапів. Спочатку, потрібно було розкласти функцію  2^x/(1-x)  в ряд Тейлора. Отриманий результат: 2^x/(1-x)=∑_(n=-1)^∞▒((-1+x)^n (-2)〖〖(ln〗⁡〖1+n)〗〗^(1+n))/(1+n)!
 Опісля я розробив функцію calculate, що використовується для знаходження суми розкладу при х = х, та кількості доданків n, що їх задає користувач:
def calculate(x, n):
    """
    Main function of the program.
    Calculates the approximation with x = x and n terms.
    >>> calculate(1, 10)
    Series diverges!
    >>> calculate(2, 5)
    -3.9996585622122782
    """
    res = 0
    for k in range(-1, n):
        try:
            res += ((-1 + x) ** k *
                    (-2) * (ln(2)) ** (1 + k)) / factorial(1 + k)
        except ZeroDivisionError:
            print('Series diverges!')
            return None
    return res
Оскільки в точці х = -1 ряд розбігається, то при х = -1 та k = -1 отримаємо ZeroDivisionError, отже ряд розбіжний
 Для коректної роботи функції було розроблено допоміжну під назвою factorial, яка працює рекурсивно та, для запобігання зайвим повторним обчисленням, використовує кешування:
@lru_cache()
def factorial(num):
    """
    Recursively calculates the factorial of a number
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    if num < 0:
        return None
    elif num <= 1:
        return 1
    return num * factorial(num - 1)
Крім функції get_input, яка отримує від користувача правильно введені значення х та кількість доданків, та main, за допомогою якої викликаються функції по черзі та виводиться інформація про результати виконання, цікаво розглянути ще number_of_terms та plot_difference.

Отже, number_of_terms:
def number_of_terms(x):
    """
    Prints out the minimum number of terms
    for the approximation to be exact
    >>> number_of_terms(10) #doctest: +ELLIPSIS
    For difference between approximation and function to be less than...
    """
    numbers_of_terms = {}
    real_res = (2 ** x) / (1 - x)
    for n in range(1, 170):
        res = calculate(x, n)
        difference = abs(real_res - res)
        if difference < 10**(-6):
            if '-6' not in numbers_of_terms:
                numbers_of_terms['-6'] = n
        if difference < 10**(-3):
            if '-3' not in numbers_of_terms:
                numbers_of_terms['-3'] = n
        if difference < 10**(-1):
            if '-1' not in numbers_of_terms:
                numbers_of_terms['-1'] = n
        if len(numbers_of_terms) == 3:
            break
    print('For difference between approximation and function to be less than:')
    if '-6' in numbers_of_terms:
        print(f"\t10^(-6): {numbers_of_terms['-6']} terms needed;")
    else:
        print("\t10^(-6): more than 170;")
    if '-3' in numbers_of_terms:
        print(f"\t10^(-3): {numbers_of_terms['-3']} terms needed;")
    else:
        print("\t10^(-3): more than 170;")
    if '-1' in numbers_of_terms:
        print(f"\t10^(-1): {numbers_of_terms['-1']} terms needed.")
    else:
        print("\t10^(-1): more than 170.")
Спочатку, потрібно розрахувати справжній результат функції 2^x/(1-x), щоб потім порівнювати з ним приближення. Опісля, змінюючи кількість доданків від 1 до 170 (Python не може зберігати надто факторіал надто великих int), функція знаходить різницю між фактичним результатом і приближенням та виводить результати.
plot_difference:
def plot_difference(x):
    """
    This function plots the difference between the approximation
    with different numbers of terms and the real function
    """
    n = abs(x * 2)
    if n < 15:
        n = 15
    n = int(round(n, 0))
    x_numbers = [calculate(x, num) for num in range(1, n)]
    y_numbers = [y for y in range(1, n)]
    plt.plot(y_numbers, x_numbers, label="Approximation",
             color='green', linestyle='dashed', linewidth=6,
             marker='o', markerfacecolor='blue', markersize=10)
    real_res = (2 ** x) / (1 - x)
    real_x = [real_res for _ in range(1, n)]
    real_y = [i for i in range(1, n)]
    plt.plot(real_y, real_x, label="Real Function", color='red', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=1)
    plt.ylabel('Result')
    plt.xlabel('Number of terms')
    plt.legend()
    plt.show()
Експериментально підбираючи масштаб графіку, дійшов висновку, що репрезентативно буде зображати від 15 до |2x| доданків, в залежності від того, скільки їх потрібно, щоб графіки наклалися (більший х – більше доданків потрібно для наближення).
Опісля, генерується список з приближень для різних значень n (кількостей доданків) та все це зображується за допомогою matplotlib.pyplot.
Приклад роботи для х = 0: 
Та для x = 50:
 
2.   Приклад роботи.
Після запуску, короткої інформації про принцип роботи програми та введення значення x та кількості доданків, користувач отримає дані про:
Кількість доданків, необхідних для того, щоб приближення було точніше, ніж 10^(-1),〖 10〗^(-3),〖 10〗^(-6);
Значення функції 2^x/(1-x) в точці х;
Наближення в точці х при n кількості доданків;
Різницю між фактичним значенням та наближенням.
 
 Крім того, згенеровано наступний графік наближення:
 
 
 

![image](https://user-images.githubusercontent.com/92430278/154859985-f1f48a5e-8fdf-43be-90f7-dc4fe9ca6caa.png)
