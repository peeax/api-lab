def assert_unchanged(api, auth, rating):
    """The owner reads the rating and finds it as it was made."""
    res = api.get(f"/api/ratings/{rating['id']}", headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot read a rating that is not theirs.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    res = api.get(f"/api/ratings/{rating['id']}", headers=other_auth)
    print("read:", res.status_code)
    assert 400 <= res.status_code <= 499
    assert_unchanged(api, auth, rating)


# Another user cannot change a rating that is not theirs.
def test_other_user_cannot_change(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 1}, headers=other_auth)
    print("change:", res.status_code)
    assert 400 <= res.status_code <= 499
    assert_unchanged(api, auth, rating)


# Another user cannot delete a rating that is not theirs.
def test_other_user_cannot_delete(api, auth, other_auth, rating):
    res = api.delete(f"/api/ratings/{rating['id']}", headers=other_auth)
    print("delete:", res.status_code)
    assert 400 <= res.status_code <= 499
    assert_unchanged(api, auth, rating)