# -*- coding: utf-8 -*-
# Copyright 2019 Bruno Toshio Sugano <brunotoshio@gmail.com>

import re

def replace_urls(text, replace_text = ''):
    return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', replace_text, text)

def replace_numbers(text, replace_text = '#'):
    return re.sub(r'[0-9]+', replace_text, text)

def replace_prices(text, replace_text = '#'):
    return re.sub(r'\d+円', replace_text, text)

def lower(text):
    return text.lower()