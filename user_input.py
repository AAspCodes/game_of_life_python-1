def get_string_input(options, prompt):
    while True:
        try:
            answer = str(input(prompt))
            if answer not in options:
                raise ImpossibleChoice
        except ImpossibleChoice:
            print(f"'{answer}' is not a possible choice, try again")
        except Exception:
            print("try again")
        else:
            break

    return answer


def get_int_input(low_end, high_end, prompt):
    while True:
        try:
            answer = int(input(prompt))
            if not (answer >= low_end and answer <= high_end):
                raise InputOutOfRange

        except InputOutOfRange:
            print(f"'{answer}' isn't in the range, try again.")
        except ValueError:
            print("try a whole number.")
        except Exception:
            print("try again.")
        else:
            break

    return answer


class bad_input(Exception):
    pass
class InputOutOfRange(Exception):
    pass


class ImpossibleChoice(Exception):
    pass
