from pymonad.tools import curry


@curry(2)
def concatenate(first, second):
    return first + second


hello = concatenate("Hello, ")


@curry(4)
def make_greeting(greeting, punctuation, ending, name):
    return greeting + punctuation + " " + name + ending


first_step = make_greeting


def main():
    print(hello("Petya"))

    final = first_step("Hello")(",")("!")
    print(final("Petya"))


if __name__ == "__main__":
    main()
