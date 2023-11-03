from datetime import datetime
import pickle, os


FILEPATH = os.getcwd()+"/evenemang.p"


class Evenemang():
    def __init__(self, name, datum, start_tid, slut_tid) -> None:
        self._name = name
        self._datum = datum
        self._start_tid = start_tid
        self._slut_tid = slut_tid
    
    def get_date(self):
        return self._datum

    def get_start_time(self):
        return self._start_tid

    def get_stop_time(self):
        return self._slut_tid


def input_datum( prompt ):
    string = input(prompt+"(YYYY/MM/DD) ")
    return datetime.strptime(string, "%Y/%m/%d")


def input_time( prompt ):
    string = input(prompt+"(HH:MM) ")
    return datetime.strptime(string, "%H:%M")


def load_file():
    if not os.path.isfile(FILEPATH):
        return
    
    with open(FILEPATH, "rb") as f:
        return pickle.load(f)


def save_file(evenemang):
    with open(FILEPATH, "wb") as f:
        evenemang = pickle.dump(evenemang, f)


def evenemang_conflict(nytt_evenemang, nuvarande_evenemang):
    for evenemang in nuvarande_evenemang:
        if evenemang.get_date() != nytt_evenemang.get_date():
            continue

        if evenemang.get_stop_time() >= nytt_evenemang.get_start_time() and evenemang.get_start_time() <= nytt_evenemang.get_stop_time():
            return True
    
    return False


def main():
    evenemang = load_file() or []

    print("Nytt evenemang: ")
    nytt_evenemang = Evenemang(input("namn: "), input_datum("datum: "), input_time("starttid: "), input_time("sluttid: "))

    if evenemang_conflict(nytt_evenemang, evenemang):
        print("Evenemanget står i konflikt med ett redan existerande evenemang!")
    else:
        evenemang.append(nytt_evenemang)
        save_file(evenemang)
        print("Nytt evenemang bokat!")


if __name__ == "__main__":
    main()