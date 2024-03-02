def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def test_prime1():
    number = 1
    assert not is_prime(number)


def test_prime2():
    number = 2
    assert is_prime(number)


def test_prime3():
    number = 3
    assert is_prime(number)


def test_prime4():
    number = 4
    assert not is_prime(number)


def test_prime5():
    number = 5
    assert is_prime(number)


def test_prime6():
    number = 6
    # Should fail
    assert is_prime(number)
