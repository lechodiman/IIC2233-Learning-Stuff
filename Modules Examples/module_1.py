globvar = 0
CHAT_ID_SET = set()


def set_globvar_to_one():
    global CHAT_ID_SET
    CHAT_ID_SET.add(21)
    if 23 in CHAT_ID_SET:
        CHAT_ID_SET.remove(23)


def print_globvar():
    print(CHAT_ID_SET)

set_globvar_to_one()
print_globvar()
