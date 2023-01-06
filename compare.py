import ast
import statistics


def comparison(files_names):
    result_score = list()   # список с нашими степенями схожести между двумя числами(количеством одинаковых токенов)

    for f in files_names:   # проходмся попарно по файлам
        text1, text2 = f[0], f[1]
        print(text1, text2)

        text1_file = ''     # записываем наш первый текст в строку
        with open(text1, "r") as file1:
            for i in file1.readlines():
                text1_file += i
        file1.close()

        text2_file = ''     # записываем наш второй текст в строку
        with open(text2, "r") as file2:
            for i in file2.readlines():
                text2_file += i
        file2.close()

        text1_file = ast.parse(text1_file)      # выполняем синтаксический анализ текста 1 в AST ноде
        text2_file = ast.parse(text2_file)      # выполняем синтаксический анализ текста 2 в AST ноде

        l1 = []     # далее добавляем в список наши токены(узлы нода)
        for i in ast.walk(text1_file):      # извлекаем из узла по типу <_ast.Name object at 0x0000016DA77E1D00> только токен Name
            amount = ''
            j = 6
            while str(i)[j] != ' ':
                amount += str(i)[j]
                j += 1
            l1.append(amount)

        l2 = []     # также и для 2 текста
        for i in ast.walk(text2_file):
            amount = ''
            j = 6
            while str(i)[j] != ' ':
                amount += str(i)[j]
                j += 1
            l2.append(amount)

        # подсчитываем количество уникальных токенов
        l1_dict = {}
        for i in l1:
            if i in l1_dict:
                l1_dict[i] += 1
            else:
                l1_dict[i] = 1

        l2_dict = {}
        for i in l2:
            if i in l2_dict:
                l2_dict[i] += 1
            else:
                l2_dict[i] = 1

        list_of_scores = []     # тут хранятся степени схожести между одинаковыми значениями словарей l1_dict и l2_dict
        for j in l2_dict:
            if j in l1_dict:
                # из 1 вычитаем разность в процентах между числами
                if l1_dict[j] > l2_dict[j]:
                    list_of_scores.append(1 - abs((l2_dict[j] - l1_dict[j]) / l1_dict[j]))
                else:
                    list_of_scores.append(1 - abs((l1_dict[j] - l2_dict[j]) / l2_dict[j]))

        print(list_of_scores)
        print(statistics.mean(list_of_scores))
        result_score.append(str(statistics.mean(list_of_scores))+'\n')      # в result_score записываем среднее из list_of_scores для пары файлов

    # значения из result_score записываем в выходной файл scores.txt
    with open('scores.txt', "w") as scores_file:
        for i in result_score:
            scores_file.write(i)
    scores_file.close()


def main():
    input_file = open('input.txt', 'r')
    files_names = []    # список с названиями файлов
    k = input_file.readlines()

    # складываем в files_names названия файлов из input
    for i in k:
        dop = list(map(str, i.split()))
        files_names.append(dop)

    comparison(files_names)


if __name__ == "__main__":
    main()
