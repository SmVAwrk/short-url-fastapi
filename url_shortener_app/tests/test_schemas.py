import datetime
import uuid

import pytest
from pydantic import ValidationError

from ..url_app.schemas import URLBase, URLCreate, URLUpdate, URL, URLInfo


def test_url_base_schema_ok():
    input_data = {
        'link': 'http://test-link.com/',
        'title': 'my_link'
    }
    data = URLBase(**input_data).dict()
    assert data == input_data


def test_url_base_schema_not_valid_link():
    input_data = {
        'link': 'not_valid_link',
        'title': 'my_link'
    }
    with pytest.raises(ValidationError):
        URLBase(**input_data)


def test_url_create_schema_ok():
    created_at = datetime.date.today()
    expected_data = {
        'link': 'http://test-link.com/',
        'title': 'my_link',
        'description': 'My description',
        'created_at': created_at,
        'link_count': 0
    }
    input_data = {
        'link': 'http://test-link.com/',
        'title': 'my_link',
        'description': 'My description',
        'created_at': created_at
    }
    data = URLCreate(**input_data).dict()
    assert data == expected_data


def test_url_create_schema_optional_field():
    input_data = {
        'link': 'http://test-link.com/',
        'title': 'my_link'
    }
    data = URLCreate(**input_data).dict()
    assert 'description' in data
    assert data['description'] is None


def test_url_create_schema_default_fields():
    input_data = {
        'link': 'http://test-link.com/',
        'title': 'my_link'
    }
    data = URLCreate(**input_data).dict()
    assert all(key in data for key in ('created_at', 'link_count'))
    assert data['created_at'] is not None
    assert data['link_count'] is not None


def test_url_update_schema_ok():
    input_data = {
        'title': 'my_link_2',
    }
    data = URLUpdate(**input_data).dict(exclude_unset=True)
    assert data == input_data


def test_url_schema_ok():
    user_uuid = uuid.uuid4()
    input_data = {
        'link': 'http://test-link.com/',
        'title': 'my_link',
        'description': 'My description',
        'id': 1,
        'user_id': user_uuid,
        'short_url': 'test'
    }
    data = URL(**input_data).dict()
    assert data == input_data


def test_url_info_schema_ok():
    created_at = datetime.date.today()
    input_data = {
        'link': 'http://test-link.com/',
        'title': 'my_link',
        'description': 'My description',
        'created_at': created_at,
        'link_count': 0,
        'id': 1,
        'short_url': 'test'
    }
    data = URLInfo(**input_data).dict()
    assert data == input_data
