from .replacer import replace_numbers, replace_prices, replace_urls, lower
from .jconverter import kana_to_full, digits_to_half, alpha_to_full, normalize_words
import logging

class JText:

    __operators = {
        'remove_url': replace_urls,
        'replace_url': replace_urls,
        'remove_prices': replace_prices,
        'replace_prices': replace_prices,
        'remove_numbers': replace_numbers,
        'replace_numbers': replace_numbers,
        'to_full_width': kana_to_full,
        'digits': digits_to_half,
        'alpha_to_full': alpha_to_full,
        'normalize': normalize_words,
        'lower': lower
    }

    def __init__(self, options = {}):
        self._pipeline = []

        default_options = {
            'dict_path': ''
        }
        self._option = {**default_options, **options}

    def process(self, pipeline):
        for step in pipeline:
            task = {}
            operation = next(iter(step))
            if operation in JText.__operators:
                task['handler'] = JText.__operators[operation]
                task['args'] = step[operation]
            else:
                logging.error(f'Invalid operation: {operation}')
                return

    def __process(self, ordered_tasks, text):
        next_input = text
        for task in ordered_tasks:
            args = task['args']
            next_input = task['handler'](next_input, **args)



    


