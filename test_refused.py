import uuid


def new_user():
    """A username nobody has used before, with the lab password."""
    name = "lab-" + uuid.uuid4().hex[:12]
    return {"username": name, "password": "Pizza-2026"}


# มี username อยุ่แล้ว refused with 400.
def test_taken_username_is_refused(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# password ผิด refused with 401.
def test_wrong_password_is_refused(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    wrong = {"username": user["username"], "password": "not-my-password"}
    res = api.post("/api/users/token/login", json=wrong)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# ไม่มี name refused with 400.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}