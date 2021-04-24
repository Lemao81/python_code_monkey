import cProfile
import cyclic_shift


def program():
    cyclic_shift.run()


cProfile.run("program()");
