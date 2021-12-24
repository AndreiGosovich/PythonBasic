
__author__ = "Госович Андрей Михайлович"

# 5.	**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла.
# Проверить работу скрипта.


def main(argv):
    if len(argv) == 4:
        _, users_file, hobbies_file, user_hobby_file = argv
        with open(users_file, "r", encoding="utf-8") as users, open(hobbies_file, "r", encoding="utf-8") as hobby,\
                open(user_hobby_file, "w", encoding="utf-8") as f:
            for person in users:
                line = hobby.readline().splitlines()
                print(f'{person.splitlines()[0]}: {line[0] if line else None}', file=f)
            if hobby.readline():
                print(f"Process finished with exit code 1")
                return 1
            print(f"Process finished with exit code 0")
            return 0
    else:
        print(f"Введено не достаточное количество параметров. Требуется 3")
        return 1


if __name__ == "__main__":
    import sys
    exit(main(sys.argv))
