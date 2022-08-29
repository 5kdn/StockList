#!/usr/bin/env python3

import os
from typing import Dict, Optional

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Stock:
    def __init__(self) -> None:
        self._get_env()
        print(f"saf::{self._SERVICE_ACCOUNT_FILE}")
        print(f"su:::{self._SHEET_URL}")
        print(f"wn:::{self._WORKSHEET_NAME}")

    def _get_SERVICE_ACCOUNT_FILE(self) -> str:
        SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
        if SERVICE_ACCOUNT_FILE is None:
            raise Exception('SERVICE_ACCOUNT_FILE is None')
        return os.path.join('/', 'tmp', 'stocklist', SERVICE_ACCOUNT_FILE)

    def _get_SHEET_URL(self) -> str:
        SHEET_URL = os.getenv('SHEET_URL')
        if SHEET_URL is None:
            raise Exception('SHEET_URL is None')
        return SHEET_URL

    def _get_WORKSHEET_NAME(self) -> str:
        WORKSHEET_NAME = os.getenv('WORKSHEET_NAME')
        if WORKSHEET_NAME is None:
            raise Exception('WORKSHEET_NAME is None')
        return WORKSHEET_NAME

    def _get_env(self) -> None:
        self._SERVICE_ACCOUNT_FILE = self._get_SERVICE_ACCOUNT_FILE()
        self._SHEET_URL = self._get_SHEET_URL()
        self._WORKSHEET_NAME = self._get_WORKSHEET_NAME()

    def get_stocks(self) -> Optional[Dict[str, str]]:
        """get stock list.

        Returns:
            Optional[Dict[str, str]]: stock list.
        """
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(self._SERVICE_ACCOUNT_FILE)
            gs = gspread.authorize(credentials)
            self._worksheet = gs.open_by_url(self._SHEET_URL).worksheet(self._WORKSHEET_NAME)
            cells = self._worksheet.get_values()
            if len(cells) <= 1:
                return None
            ret = {}
            for id, name, price, inventory, remarks in cells[1:]:
                ret[id] = {
                    'name': name,
                    'price': price,
                    'inventory': inventory,
                    'remarks': remarks,
                }
            return ret
        except Exception:
            return None
