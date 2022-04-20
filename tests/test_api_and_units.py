from app.logic import daily_required_calories


def test_home_get(client):
    """Test GET request and check if fields in template"""
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'gender' in resp.data
    assert b'mass' in resp.data
    assert b'height' in resp.data
    assert b'age' in resp.data
    assert b'food' in resp.data


def test_home_post(client):
    """Test POST request if not field"""
    resp = client.post('/', data=dict(gender='male',
                                      mass=75,
                                      height=80,
                                      age=30))
    assert resp.status_code == 400


def test_daily_required_calories():
    """
    Test daily_required_calories function. Must return only float.
    Bodies with the same parameters but different gender needs not the same amount of calories.
    """
    res_male = daily_required_calories(gender='male', mass=75, height=80, age=30)
    res_female = daily_required_calories(gender='female', mass=75, height=80, age=30)
    assert isinstance(res_male, float)
    assert res_male != res_female
    assert res_male == 1295.4569999999999
