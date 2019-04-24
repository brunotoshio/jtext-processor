#!/usr/bin/env python
# -*- encoding: utf-8 -*-
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
        {'replace_numbers'}
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
        {'replace_prices'}
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
        {'replace_url'}
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
