while True:
    try:
        x = int(input('数字を入れてください: '))
        print('great!')
        break
    except (TypeError, NameError, ValueError):
        print("数字じゃないんじゃ")

    print("もう一度！\n")