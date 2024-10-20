import timeit
import pandas as pd
import matplotlib.pyplot as plt
from boyer_moore import boyer_moore
from knuth_morris_pratt import knuth_morris_pratt
from rabin_karp import rabin_karp

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8',errors="ignore") as file:
        return file.read()

text1 = load_text('C:/Algoritmos/goit-algo-hw-05/Task3/article1.txt')
text2 = load_text('C:/Algoritmos/goit-algo-hw-05/Task3/article2.txt')

existing_substring = 'алгоритми сортування'
non_existing_substring = 'віддалена галактика'

def run_test(text, pattern, algorithm):
    # Використання globals для доступу до функції
    setup_code = f"from {algorithm.__module__} import {algorithm.__name__}"
    stmt_code = f"{algorithm.__name__}(text, pattern)"
    # Передача тексту та патерну як глобальних змінних
    times = timeit.repeat(setup=setup_code, stmt=stmt_code, repeat=5, number=10, globals={'text': text, 'pattern': pattern})
    return min(times)

# Список алгоритмів
algorithms = {
    'Boyer-Moore': boyer_moore,  
    'Knuth-Morris-Pratt': knuth_morris_pratt,
    'Rabin-Karp': rabin_karp
}

# Функція для побудови графіків результатів
def plot_results(article_text, article_name, ax):
    results = {}
    for name, func in algorithms.items():
        results[name] = {
            'Existing substring': run_test(article_text, existing_substring, func),
            'Non-existing substring': run_test(article_text, non_existing_substring, func),
        }

    # Перетворення результатів у DataFrame
    df = pd.DataFrame(results).T
    df.columns = ['Existing Substring', 'Non-existing Substring']

    # Побудова графіка
    df.plot(kind='bar', ax=ax, title=f"Performance of Substring Search Algorithms ({article_name})")
    ax.set_xlabel("Algorithm")
    ax.set_ylabel("Time (seconds)")
    ax.tick_params(rotation=45)

    print(f"\n{article_name} results:")
    print(df)

# Створення фігури та осі для підграфіків
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Побудова результатів для кожної статті
plot_results(text1, 'Article 1', axs[0])
plot_results(text2, 'Article 2', axs[1])

plt.tight_layout()
plt.show()
