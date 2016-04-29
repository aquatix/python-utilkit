"""
Printing helper functions, for pretty printing/formatting of data and more
"""
import datetimeutil

def to_even_columns(data, headers=None):
    """
    Nicely format the 2-dimensional list into evenly spaced columns
    """
    result = ''
    col_width = max(len(word) for row in data for word in row) + 2  # padding
    if headers:
        header_width = max(len(word) for row in headers for word in row) + 2
        if header_width > col_width:
            col_width = header_width

        result += "".join(word.ljust(col_width) for word in headers) + "\n"
        result += '-' * col_width * len(headers) + "\n"

    for row in data:
        result += "".join(word.ljust(col_width) for word in row) + "\n"
    return result


def to_smart_columns(data, headers=None, padding=2):
    """
    Nicely format the 2-dimensional list into columns
    """
    result = ''
    col_widths = []
    for row in data:
        col_counter = 0
        for word in row:
            try:
                col_widths[col_counter] = max(len(word), col_widths[col_counter])
            except IndexError:
                col_widths.append(len(word))
            col_counter += 1

    if headers:
        col_counter = 0
        for word in headers:
            try:
                col_widths[col_counter] = max(len(word), col_widths[col_counter])
            except IndexError:
                col_widths.append(len(word))
            col_counter += 1

    # Add padding
    col_widths = [width + padding for width in col_widths]
    total_width = sum(col_widths)

    if headers:
        col_counter = 0
        for word in headers:
            result += "".join(word.ljust(col_widths[col_counter]))
            col_counter += 1
        result += "\n"
        result += '-' * total_width + "\n"

    for row in data:
        col_counter = 0
        for word in row:
            result += "".join(word.ljust(col_widths[col_counter]))
            col_counter += 1
        result += "\n"
    return result


def progress_bar(items_total, items_progress, columns=40, base_char='.', progress_char='#', percentage=False, prefix='', postfix=''):
    """
    Print a progress bar of width `columns`
    """
    bins_total = int(float(items_total) / columns) + 1
    bins_progress = int((float(items_progress) / float(items_total)) * bins_total) + 1
    progress = prefix
    progress += progress_char * bins_progress
    progress += base_char * (bins_total - bins_progress)
    if percentage:
        progress_percentage = float(items_progress) / float(items_total) * 100
        # Round the percentage to two decimals
        postfix = ' ' + str(round(progress_percentage, 2)) + '% ' + postfix
    progress += postfix
    return progress


def merge_x_y(collection_x, collection_y, filter_none=False):
    """
    Merge two lists, creating a dictionary with key `label` and a set x and y
    """
    data = {}
    for item in collection_x:
        #print item[0:-1]
        #print item[-1]
        label = datetimeutil.tuple_to_string(item[0:-1])
        if filter_none and label == 'None-None':
            continue
        data[label] = {'label': label, 'x': item[-1], 'y': 0}
    for item in collection_y:
        #print item
        label = datetimeutil.tuple_to_string(item[0:-1])
        if filter_none and label == 'None-None':
            continue
        try:
            data[label]['y'] = item[-1]
        except KeyError:
            data[label] = {'label': label, 'x': 0, 'y': item[-1]}

    # Keys are not sorted
    return data


def get_max_x_y(data):
    max = 0
    for item in data:
        if data[item]['x'] > max:
            max = data[item]['x']
        if data[item]['y'] > max:
            max = data[item]['y']
    return max


def x_vs_y(collection_x, collection_y, title_x=None, title_y=None, width=43, filter_none=False):
    """
    Print a histogram with bins for x to the left and bins of y to the right
    """
    data = merge_x_y(collection_x, collection_y, filter_none)

    max_value = get_max_x_y(data)
    bins_total = int(float(max_value) / width) + 1

    if title_x is not None and title_y is not None:
        headers = [title_x, title_y]
    else:
        headers = None
    result = []
    # Sort keys
    for item in sorted(data):
        #result.append([item, str(data[item]['x']) + '|' + str(data[item]['y'])])
        bins_x = int((float(data[item]['x']) / float(max_value)) * bins_total) + 1
        bins_y = int((float(data[item]['y']) / float(max_value)) * bins_total) + 1
        print(bins_x)
        print(bins_y)
        #result.append([item, str(data[item]['x']), str(data[item]['y'])])
        result.append([item, '*' * bins_x, '*' * bins_y])
    result = to_smart_columns(result, headers=headers)
    return result
