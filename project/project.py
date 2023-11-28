import sqlite3
import sys


def main():
    if not is_connected("database.db"):
        print("Connection error!")
    while True:
        try:
            to_do = input("Insert data(i)? or get password(g)? ").strip()

            if to_do in ["i", "g"]:
                locate = input("Enter Locate: ")
                if to_do == "i" and check_locate(locate):
                    print("Sorry, this locate is exist!")
                    sys.exit(0)
                elif to_do == "i" and not check_locate(locate):
                    username = input("Enter username: ").strip()
                    password = input("Enter password: ").strip()
                    insert_data(username, password, locate)
                    sys.exit(0)
                elif to_do == "g" and not check_locate(locate):
                    print("Sorry, this locate is not exist!")
                    sys.exit(0)
                elif to_do == "g" and check_locate(locate):
                    Username, Password = get_data(locate)
                    print(f"Username is '{Username}' and password is '{Password}' ")
                    sys.exit(0)
                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("Invalid input!")
            continue
        except (EOFError, KeyError, KeyboardInterrupt):
            print()
            sys.exit()


def is_connected(database_path):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS savepass (username VARCHAR, password VARCHAR, loca VARCHAR)"""
        )

        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False


def insert_data(user, pw, l):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO savepass (username, password, loca) VALUES(?, ?, ?)''',
        (user, pw, l)
    )
    conn.commit()
    conn.close()
    print("Data entered successfully.")


def get_data(l):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    data = cursor.execute(f'''SELECT username, password FROM savepass WHERE loca = '{l}' ''')
    data= data.fetchall()
    user, pw = data[0][0], data[0][1]
    return user, pw



def check_locate(l):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        result = cursor.execute(f'''SELECT * FROM savepass WHERE loca = '{l}' ''')
        result = result.fetchall()
        conn.close()

        if len(result) > 0:
            return True
        else:
            return False

    except ValueError:
        sys.exit("Invalid input!")
    except sqlite3.Error as e:
        sys.exit(f"Error: {e}")



if __name__ == "__main__":
    main()
