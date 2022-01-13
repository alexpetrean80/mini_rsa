# Large Prime Generation for RSA
import random

# List of primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def n_random(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def get_low_level_prime(n):
    # Generating a prime candidate divisible by first primes
    while True:
        # Obtain a random number
        candidate_prime = n_random(n)

        # Test divisibility by pre-generated primes
        for divisor in first_primes_list:
            if candidate_prime % divisor == 0:
                break
        else:
            return candidate_prime


def is_miller_rabin_passed(candidate):
    # 20 iterations of Rabin Miller Primality test
    s = 0
    t = candidate - 1
    while t % 2 == 0:
        t >>= 1
        s += 1
    assert (2 ** s * t == candidate - 1)

    def trial_composite(round_tester):
        if pow(round_tester, t, candidate) == 1:
            return False
        a = pow(round_tester, t, candidate)
        for i in range(s):
            if a == 1 and i == 0:
                return False
            if a == candidate - 1:
                return False
            a = (a*a) % candidate
        return True

    number_of_rabin_trials = 20

    used_testers = set()

    for i in range(number_of_rabin_trials):

        while True:
            round_tester = random.randrange(2, candidate)
            if round_tester not in used_testers:
                used_testers.add(round_tester)
                break

        if trial_composite(round_tester):
            return False
    return True


def generating_primes(n):
    ok = 0
    p = 0
    q = 0
    while True:
        f = open("./p_and_q.txt", "a")
        prime_candidate = get_low_level_prime(n)
        if not is_miller_rabin_passed(prime_candidate):
            continue
        else:
            f.write(str(prime_candidate) + '\n')
            if ok == 0:
                p = prime_candidate
            else:
                q = prime_candidate
            ok += 1
        if ok == 2:
            break
    f.close()
    return p, q


# if __name__ == '__main__':
#    generating_primes(300)
