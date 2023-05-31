import pickle
import os

def input_scores():
    print('[점수 입력]')
    scores = []
    i = 1
    while True:
        a = int(input(f'#{i}? '))
        if a < 0:
            break
        scores.append(a)
        i += 1
    return scores

def get_average(lst):
    all_scores = 0
    for i in range(len(lst)):
        all_scores += lst[i]
    return all_scores / len(lst)

def show_scores(lst, avg):
    print('[점수 출력]')
    print('개인점수: ', end='')
    for i in range(len(lst)):
        print(f'{lst[i]} ', end='')
    print()
    print(f'평균: {avg}')

def save_scores(scores):
    with open('score.bin', 'wb') as file:
        pickle.dump(scores, file)

def load_scores():
    if os.path.exists('score.bin'):
        with open('score.bin', 'rb') as file:
            scores = pickle.load(file)
            show_scores(scores, get_average(scores))

scores = input_scores()
average = get_average(scores)
show_scores(scores, average)
save_scores(scores)
load_scores()
