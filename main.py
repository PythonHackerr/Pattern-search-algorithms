from funcs import naive, kmp, kr
import tools
import sys


def collect_stats(func, words, steps=10, values_step=100, repeats=1):
    measures = {}
    for i in range(steps+1):
        nvalues = i*values_step
        selected_words = words[:nvalues]
        measures[nvalues] = tools.measure_time(
            lambda: func(selected_words), repeats)
    return measures


def find_words(find_func, words):
    for word in words:
        find_func(word)


def main():
    sys.setrecursionlimit(10000)
    words = tools.get_words_list(1500, 'pan-tadeusz.txt')
    stats_naive = collect_stats(lambda: find_words(naive), words, repeats=5)
    stats_kmp = collect_stats(lambda: find_words(kmp), words, repeats=5)
    stats_kr = collect_stats(lambda: find_words(kr), words, repeats=5)
    data = {
        'naive': stats_naive,
        'kmp': stats_kmp,
        'kr': stats_kr
    }
    tools.draw_multiple('Find pattern', 'Words, n', 'Time, s', data, 'find_pattern')


if __name__ == "__main__":
    main()
