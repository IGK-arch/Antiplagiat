import ast
import statistics


def refactor(files_names):
    result_score = list()

    for f in files_names:
        text1, text2 = f[0], f[1]
        print(text1, text2)

        text1_file = ''
        with open(text1, "r") as file1:
            for i in file1.readlines():
                text1_file += i
        file1.close()

        text2_file = ''
        with open(text2, "r") as file2:
            for i in file2.readlines():
                text2_file += i
        file2.close()

        text1_file = ast.parse(text1_file)
        text2_file = ast.parse(text2_file)

        l1 = []
        for i in ast.walk(text1_file):
            amount = ''
            j = 6
            while str(i)[j] != ' ':
                amount += str(i)[j]
                j += 1
            l1.append(amount)

        l2 = []
        for i in ast.walk(text2_file):
            amount = ''
            j = 6
            while str(i)[j] != ' ':
                amount += str(i)[j]
                j += 1
            l2.append(amount)

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

        list_of_scores = []
        for j in l2_dict:
            if j in l1_dict:
                if l1_dict[j] > l2_dict[j]:
                    list_of_scores.append(1 - abs((l2_dict[j] - l1_dict[j]) / l1_dict[j]))
                else:
                    list_of_scores.append(1 - abs((l1_dict[j] - l2_dict[j]) / l2_dict[j]))

        print(list_of_scores)
        print(statistics.mean(list_of_scores))
        result_score.append(str(statistics.mean(list_of_scores))+'\n')

    with open('scores.txt', "a") as scores_file:
        for i in result_score:
            scores_file.write(i)
    scores_file.close()


def main():
    input_file = open('input.txt', 'r')
    files_names = []
    k = input_file.readlines()
    for i in k:
        dop = list(map(str, i.split()))
        files_names.append(dop)
    print(files_names)
    refactor(files_names)


if __name__ == "__main__":
    main()
