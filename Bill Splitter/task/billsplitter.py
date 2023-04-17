import random


def friends_dont_join():
    print('No one is joining for the party')
    exit()


def get_num_friends():
    try:
        print('Enter the number of friends joining (including you):')
        _num_friends = int(input())
        if _num_friends <= 0:
            raise ValueError
        return _num_friends
    except ValueError:
        friends_dont_join()


def get_friends_party(_num_friends: int):
    _friends = {}
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(int(_num_friends)):
        _friends[input()] = 0
    return _friends


def get_bill_total():
    try:
        print('Enter the total bill value:')
        _bill_total = int(input())
        if _bill_total <= 0:
            raise ValueError
        return _bill_total
    except ValueError:
        friends_dont_join()


def select_lucky_friend(_friends):
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == 'Yes':
        random_num = random.randint(0, int(num_friends))
        _lucky_friend = list(_friends.keys())[random_num]
        print(f'{_lucky_friend} is the lucky one!')
        return _lucky_friend

    else:
        print('No one is going to be lucky')
        return None


def adjust_bill(_friends, _lucky_friend, _bill_total):
    if _lucky_friend is None:
        _friends = dict.fromkeys(_friends, round(int(_bill_total) / len(_friends), 2))
    else:
        _friends = dict.fromkeys(_friends, round(int(_bill_total) / (len(_friends) - 1), 2))
        _friends[_lucky_friend] = 0
    print(_friends)


num_friends = get_num_friends()
friends = get_friends_party(num_friends)
bill_total = get_bill_total()
lucky_friend = select_lucky_friend(friends)
adjust_bill(friends, lucky_friend, bill_total)
