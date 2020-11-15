import StudentSolution as e

def assert_throws(fun):
    try:
        fun()
    except:
        return

    assert False

# Valid
assert 123 == e.evaluate_postfix("123")
assert 2 == e.evaluate_postfix("1 1 +")
assert 40 == e.evaluate_postfix("20 2 *")
assert 3 == e.evaluate_postfix("16 5 /")
assert 0 == e.evaluate_postfix("5 16 /")
assert 40 == e.evaluate_postfix("44 4 -")
assert 2040 == e.evaluate_postfix("51 3 41 14 - + 10 + *")
assert 6 == e.evaluate_postfix("1 1 1 1 1 1 + + + + +")
assert 2 == e.evaluate_postfix("1 1 + 1 + 1 + 2 /")
assert 2 == e.evaluate_postfix("5 5 + 2 / 5 * 5 + 5 - 5 5 + /")
assert 0 == e.evaluate_postfix("5 10 - 5 +")

# Invalid
assert_throws(lambda: e.evaluate_postfix("1 +"))
assert_throws(lambda: e.evaluate_postfix("1 1 + 1"))
assert_throws(lambda: e.evaluate_postfix("+ + +"))
assert_throws(lambda: e.evaluate_postfix("invalid"))
assert_throws(lambda: e.evaluate_postfix("5 5 5 5 5"))
assert_throws(lambda: e.evaluate_postfix("5 5 5 - /"))
