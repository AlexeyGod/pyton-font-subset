from fontTools.subset import main

# run this `python create_subset.py`

# Список Unicode кодов из вашего CSS
unicodes = [
    'U+E0CD',  # phone
    'U+E145',  # add
    'U+E15B',  # remove
    'U+E313',  # keyboard_arrow_down
    'U+E314',  # keyboard_arrow_left
    'U+E315',  # keyboard_arrow_right
    'U+E55F',  # place
    'U+E5CD',  # close
    'U+E5D8',  # arrow_upward
    'U+E5DB',  # arrow_downward
    'U+E5DD',  # arrow_forward
    'U+E5DE',  # arrow_back
    'U+E853',  # account_circle
    'U+E87E',  # favorite_border
    'U+E8CC',  # shopping_cart
    'U+E9EC',  # swipe
    'U+EA77'   # login
]

# Сохраняем коды в файл
with open('unicodes.txt', 'w', encoding='utf-8') as f:
    for code in unicodes:
        f.write(f"{code}\n")

print("Файл unicodes.txt создан")

# Создаем подмножество шрифта
main([
    'MaterialSymbolsOutlined.ttf',
    '--output-file=MaterialSymbolsOutlined.woff2',
    '--unicodes-file=unicodes.txt',
    '--flavor=woff2'
])

print("Подмножество шрифта создано: MaterialSymbolsOutlined.woff2")