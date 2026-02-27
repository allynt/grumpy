from http import HTTPStatus

def test_robots_txt(client):

    response = client.get("/robots.txt")
    assert response.status_code == HTTPStatus.OK
    assert response["content-type"] == "text/plain"
    assert response.content.startswith(b"# robots.txt\n")