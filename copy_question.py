import importlib

curr_module = importlib.import_module('best_time_to_buy_and_sell_stock')

question_text = f'{curr_module.source_url}'

print(question_text)