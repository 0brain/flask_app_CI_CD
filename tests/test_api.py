def test_home_get(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'gender' in resp.data
    assert b'mass' in resp.data
    assert b'height' in resp.data
    assert b'age' in resp.data
    assert b'food' in resp.data


def test_home_post(client):
    resp = client.post('/', data=dict(gender='male',
                                      mass=75,
                                      height=80,
                                      age=30))
    assert resp.status_code == 400
