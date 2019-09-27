#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import logging


LOGGER = logging.getLogger(__name__)
TIMEOUT = 60


class WebTest(object):

    def setup_method(self, method):
        '''
        Setup method to run before each test case
        '''
        print ""

    def teardown_method(self, method):
        '''
        Setup method to run after each test case
        '''
