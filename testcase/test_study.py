import pytest
from conftest import http
from common import commonData
import allure

class Teststudy:
    @allure.feature('获取学习动态')
    @allure.story('成功获取')
    @pytest.mark.usefixtures('login')
    def test_s(self,login):

        login
        path='api/courses/v3/trends'
        http.get(path=path)