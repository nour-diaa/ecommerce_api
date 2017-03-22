from api import app
from model import Item as ItemModel
from peewee import SqliteDatabase
from http.client import CREATED
from http.client import NO_CONTENT
from http.client import NOT_FOUND
from http.client import OK
from http.client import INTERNAL_SERVER_ERROR
from model import connect, close

TEST_ITEM={
    'name': 'mario',
    'price': 20.20,
    'description': 'svariati mariii'
}

class TestItems:
    @classmethod
    def setup_class(cls):
        ItemModel._meta.database = SqliteDatabase(':memory:')
        connect()
        cls.app = app.test_client()

    @classmethod
    def teardown_class(cls):
        close()

    def test_post_item__success(self):
        resp = self.app.post('/items/', data=TEST_ITEM)
        assert resp.status_code == CREATED
        assert len(ItemModel.select()) == 1

    


