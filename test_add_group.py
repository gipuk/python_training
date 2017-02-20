# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.sesion.enter_login(username="admin", password="secret")
    app.group.create(Group(name="test python", header="test", footer="testtest"))
    app.sesion.logout()


def test_add_empty_group(app):
    app.sesion.enter_login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.sesion.logout()