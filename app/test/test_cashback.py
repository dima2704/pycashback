
def cashback(amount):
    percent = 0.05
    limit = 3_000
    result = amount * percent
    if result > limit:
        return limit
    return result

def test_cashback_above_limit():
    resilt = cashback(1_000_000)
    assert 3_000 == resilt

