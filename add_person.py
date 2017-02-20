# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from person import Person


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return  fixture

def test_add_person(app):
    app.open_home_page()
    app.enter_login( username = "admin", password = "secret")
    app.add_osoba(Person(first_name="Jan", middle="Maria", last="sfvdfgvfd", nick="dsfdsfds", title="senor",
                       company="werwerwe", comaddr="vdfgdfgdfbdfd", homenr="78578865", mobile="454535354354",
                       worknr="7567456464", faxnr="brak", email_1="qweqwe@wew.pl", email_2="weweweew@wew.pl",
                       email_3="asasas@weew.pl", home_page="www.test.com", year_b="1980", year_a="1980",
                       home_add="erwerewrwer", home_phone="sdfsdfds", note="sdfffsd"))
    app.go_to_home()
    app.logout()


