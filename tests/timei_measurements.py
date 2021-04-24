from common import right_shift_string_extended
import timeit


def run():
    right_shift_string_extended('lsfjalsjdflajsflkjaslfjlasjflkajsldfkjaskdfjlasjdflajslfasjfd')


timer = timeit.Timer("run()", globals={"run": run})
print(timer.timeit())
