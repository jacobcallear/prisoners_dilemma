'''Sort `defaultdict` and print in markdown table format.'''
from textwrap import dedent


def sort_by_value(dictionary):
    '''Returns a sorted list from a dictionary in order of ascending values.'''
    return sorted(
        dictionary.items(),
        key=lambda x: dictionary[x[0]],
        reverse=True
    )


def __to_markdown_row(text):
    return f'| {text} |'


def convert_to_table(dictionary, heading_1, heading_2):
    '''Converts a dictionary to a table-like string.'''
    # Print table header
    left_align = 15
    right_align = 5
    width = left_align + right_align + 3

    # Add table header
    rows = []
    header = __to_markdown_row(
        f'{heading_1:<{left_align}} | {heading_2:>{right_align}}'
    )
    rows.append(header)
    rows.append(__to_markdown_row('-' * width))

    # Add table rows
    for strategy, score in dictionary:
        rows.append(__to_markdown_row(f'{strategy:<15} | {score:>5}'))
    return '\n'.join(rows)
