import ast
import statistics


def read_file(file_name: str):
    with open(file_name) as f:
        file = f.read()
    return file


def write(result_score: list):
    with open('scores.txt', "w") as scores_file:
        for i in result_score:
            scores_file.write(i)
    scores_file.close()


def get_token(text_file):
    token_list = []  # далее добавляем в список наши токены(узлы нода)
    for i in ast.walk(text_file):  # извлекаем из узла по типу <_ast.Name object at 0x0000016DA77E1D00> только <class '_ast.Module'>
        amount = type(i)
        token_list.append(amount)
    return token_list


def token_count(text_file):
    l_dict = {}
    for i in get_token(text_file):  # Обращаемся к функции get_token дл получения списка с токенами в формате <class '_ast.Module'>, а далее считываем их количество
        if i in l_dict:
            l_dict[i] += 1
        else:
            l_dict[i] = 1
    return l_dict   # возвращаем словарь с количеством каждого токена


def score_similarity_count(original_dict: dict, plagiat_dict):
    list_of_scores = []  # тут хранятся степени схожести между одинаковыми значениями словарей l1_dict и l2_dict
    for j in plagiat_dict:
        if j in original_dict:
            # из 1 вычитаем разность в процентах между числами
            if original_dict[j] > plagiat_dict[j]:
                list_of_scores.append(1 - abs((plagiat_dict[j] - original_dict[j]) / original_dict[j]))
            else:
                list_of_scores.append(1 - abs((original_dict[j] - plagiat_dict[j]) / plagiat_dict[j]))

    return list_of_scores


def comparison(files_names):
    result_score = list()  # список с нашими степенями схожести между двумя числами(количеством одинаковых токенов)

    for f in files_names:  # проходмся попарно по файлам
        text1, text2 = f[0], f[1]
        print(text1, text2)

        text1_file = ast.parse(read_file(text1))  # выполняем синтаксический анализ текста 1 в AST ноде
        text2_file = ast.parse(read_file(text2))  # выполняем синтаксический анализ текста 2 в AST ноде

        # подсчитываем количество уникальных токенов и получаем 2 словаря
        l1_dict = token_count(text1_file)
        l2_dict = token_count(text2_file)

        list_of_scores = score_similarity_count(l1_dict, l2_dict)

        print(statistics.mean(list_of_scores))
        result_score.append(str(statistics.mean(list_of_scores)) + '\n')  # в result_score записываем среднее из list_of_scores для пары файлов

    # значения из result_score записываем в выходной файл scores.txt
    write(result_score)


def main():
    input_file = open('input.txt', 'r')
    k = input_file.readlines()
    files_names = [i.split() for i in k]  # список с названиями файлов из input.txt

    comparison(files_names)


if __name__ == "__main__":
    main()
