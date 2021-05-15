import re


def has_html(string: str):
    return '<' in string


def slice_comment(string: str):
    return string[string.index('-->') + 3:]


def slice_end_tag(string: str):
    return string[string.index('>') + 1:]


def slice_to_tag(string: str):
    return string[string.index('<'):]


def is_comment(string: str):
    return string.startswith('<!--')


def is_end_tag(string: str):
    return string.startswith('</')


def is_empty_tag(string: str):
    return string[string.index('>') - 1] == '/'


def parse_tag(string: str):
    print_tag_name(get_tag_name(string))
    parse_attributes(string)
    return string[string.index('>') + 1:]


def parse_attributes(string: str):
    attribute_area = string[:string.index('>')]
    attribute_matches = re.findall('\s([\w-]+)=', attribute_area)
    value_matches = re.findall('"(.*?)"', attribute_area)
    for index, attribute in enumerate(attribute_matches):
        print_attribute_name(attribute)
        print_value(value_matches[index])


def get_tag_name(string: str):
    match = re.match('<(\w+)', string)
    return match.group(1)


def print_tag_name(string: str):
    print(string)


def print_attribute_name(string: str):
    print('-> {0}'.format(string), end=" ")


def print_value(string: str):
    print('> {0}'.format(string))


def parse_next_html_tag(remaining: str):
    if not has_html(remaining):
        return

    remaining = slice_to_tag(remaining)

    if is_comment(remaining):
        parse_next_html_tag(slice_comment(remaining))
    elif is_end_tag(remaining):
        parse_next_html_tag(slice_end_tag(remaining))
    else:
        parse_next_html_tag(parse_tag(remaining))


if __name__ == '__main__':
    n = int(input())
    lines = []
    for i in range(n):
        lines.append(input())

    parse_next_html_tag(' '.join(lines))
