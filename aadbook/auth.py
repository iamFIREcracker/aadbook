#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import json
from datetime import datetime
from dateutil.parser import parse

import adal

log = logging.getLogger(__name__)

AUTHORITY_HOST_URI = 'https://login.microsoftonline.com'
TENANT = 'common'
AUTHORITY_URI = AUTHORITY_HOST_URI + '/' + TENANT
RESOURCE_URI = 'https://graph.microsoft.com'
CLIENT_ID = '9f461068-2572-465b-9377-a5c284b326d1'


class Auth(object):
    def __init__(self, auth_file):
        self.context = adal.AuthenticationContext(AUTHORITY_URI,
                                                  api_version=None)
        self.auth_file = auth_file
        self.creds = self._read_creds()

    def _read_creds(self):
        try:
            with open(self.auth_file, 'r') as f:
                return json.load(f)
        except IOError:
            log.debug("Failed to read auth_file %s" % self.auth_file)
            return None

    @property
    def invalid(self):
        if not self.creds:
            return True

        expires_on = parse(self.creds['expiresOn'])
        return expires_on < datetime.now()

    def authenticate(self):
        if self.creds:
            refresh_token = self.creds['refreshToken']
            token = self.context.acquire_token_with_refresh_token(
                refresh_token,
                CLIENT_ID,
                RESOURCE_URI)
        else:
            code = self.context.acquire_user_code(RESOURCE_URI,
                                                  CLIENT_ID)
            print(code['message'])
            token = self.context.acquire_token_with_device_code(RESOURCE_URI,
                                                                code,
                                                                CLIENT_ID)
        self._save_creds(token)

    def _save_creds(self, data):
        with open(self.auth_file, 'w') as f:
            json.dump(data, f)


if __name__ == '__main__':
    print Auth('~/.aadbook_auth.json').authenticate()