def num(value: str) -> str:
    format_str = 'Вы ввели {} число {}'
    if value.isdigit():
        return format_str.format('целое положительное', value)
    try:

        if '-' in value and '.' in value:
            value = float(value)
            return format_str.format('отрицательное дробное', value)

        elif '.' in value:
            value = float(value)
            return format_str.format('положительное дробное', value)

        elif '-' in value and '.' not in value:
            value = int(value)
            return format_str.format('отрицательное целое', value)

    except ValueError:
        return format_str.format('неправильное', value)

    else:
        return format_str.format('неправильное', value)
