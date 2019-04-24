#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import logging
from unittest import mock

from jtextprocessor import processor


@mock.patch('jtextprocessor.processor.alpha_to_full')
def test_class_jtext_alpha_to_full(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'alpha_to_full'}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.digits_to_half')
def test_class_jtext_digits(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'digits'}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.kana_to_full')
def test_class_jtext_to_full_width(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'to_full_width'}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.normalize_words')
def test_class_jtext_normalize(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'normalize'}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.lower')
def test_class_jtext_lower(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'lower'}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.replace_numbers')
def test_class_jtext_replace_numbers(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'replace_numbers': {'replace_text': 'n'}}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.replace_numbers')
def test_class_jtext_remove_numbers(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'remove_numbers'}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.replace_prices')
def test_class_jtext_replace_prices(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'replace_prices': {'replace_text': '$'}}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.replace_prices')
def test_class_jtext_remove_prices(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'remove_prices'}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.replace_urls')
def test_class_jtext_replace_url(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'replace_url': {'replace_text': 'url'}}
    ])
    jtext.run('kore')
    assert mocked.called


@mock.patch('jtextprocessor.processor.replace_urls')
def test_class_jtext_remove_url(mocked):
    jtext = processor.JText()
    jtext.prepare([
        {'remove_url'}
    ])
    jtext.run('kore')
    assert mocked.called


def test_class_jtext_prepare():
    jtext = processor.JText()
    list_of_tasks = [
        {'alpha_to_full'},
        {'digits'},
        {'to_full_width'},
        {'normalize'},
        {'lower'},
        {'replace_numbers': {'replace_text': 'n'}},
        {'remove_numbers'},
        {'replace_prices': {'replace_text': '$'}},
        {'remove_prices'},
        {'replace_url': {'replace_text': 'url'}},
        {'remove_url'}
    ]
    assert len(list_of_tasks) == len(jtext._operators.keys())
    jtext.prepare(list_of_tasks)
    assert len(jtext._pipeline) == len(list_of_tasks)


def test_class_jtext_prepare_error(caplog):
    with caplog.at_level(logging.ERROR):
        jtext = processor.JText()
        jtext.prepare([{'non_existing_task'}])
        assert ['Invalid operation: non_existing_task'] == [rec.message for rec in caplog.records]

