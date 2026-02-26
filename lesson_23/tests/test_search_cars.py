import pytest

BASE_URL = "http://127.0.0.1:8080"


def _is_sorted(items, key):
    values = [x.get(key, 0) for x in items]
    return values == sorted(values)


@pytest.mark.usefixtures("auth_session")
class TestCarsSearch:
    @pytest.mark.parametrize(
        "sort_by,limit",
        [
            ("price", 5),
            ("year", 10),
            ("engine_volume", 3),
            ("brand", 7),
            ("price", None),
            (None, 4),
        ],
    )
    def test_search_cars_sort_limit(self, auth_session, logger, sort_by, limit):
        url = f"{BASE_URL}/cars"
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = str(limit)

        logger.info(f"GET {url} params={params}")
        resp = auth_session.get(url, params=params, timeout=10)
        logger.info(f"RESPONSE status={resp.status_code}, body={resp.text}")

        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        assert len(data) > 0

        if limit is not None:
            assert len(data) <= limit

        if sort_by is not None:
            assert _is_sorted(data, sort_by), f"Not sorted by {sort_by}"