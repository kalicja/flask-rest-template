import json

import pytest
from assertpy import assert_that
from flask_rest_demo.repository.hello_repo import HelloRepo, Hello, HelloEncoder


class TestHelloRepo:

    @pytest.fixture
    def subject(self):
        hello_repo=HelloRepo()
        hello_repo.hellos={0: Hello('hi all', 'alicja')}
        hello_repo.last_id=0
        yield hello_repo


    def test_get_all(self, subject):
        actual = subject.get_all()

        assert_that(actual).is_length(1)
        assert_that(actual).is_equal_to([Hello('hi all', 'alicja')])

    @pytest.mark.parametrize(
        'id,expected',
        [pytest.param(-1, None),
         pytest.param(0, Hello('hi all', 'alicja')),
         pytest.param(2, None)]
    )
    def test_get(self, subject, id, expected):
        actual = subject.get(id)

        assert_that(actual).is_equal_to(expected)


    def test_save(self, subject):
        last_id=subject.last_id

        subject.save(Hello('hi u', 'lola'))

        all = subject.get_all()

        assert_that(all).is_length(2)
        assert_that(last_id+1).is_equal_to(subject.last_id)
        assert_that(all).is_equal_to([Hello('hi all', 'alicja'), Hello('hi u', 'lola')])

    def test_delete(self, subject):
        last_id=subject.last_id

        subject.delete(0)

        all = subject.get_all()

        assert_that(all).is_length(0)
        assert_that(last_id).is_equal_to(subject.last_id)
        assert_that(all).is_equal_to([])
