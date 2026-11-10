import pytest

# Stars 1 and 5 are saved with 200, stars 0 and 6 are refused with 400 and leave the rating unchanged.
@pytest.mark.parametrize(
    "stars, expected_status",
    [(0, 400), (1, 200), (5, 200), (6, 400)],
)
def test_update_stars_boundaries(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    expected_stars = stars if expected_status == 200 else rating["stars"]
    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json()["stars"] == expected_stars