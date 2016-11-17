url = "ho  o ps"
modded = url.replace(' ', '%20')

string_array = list(url) + [' '] * url.count(' ') * 2

codes = {' ': '%20'}


def urlify(s, len_s):
    new_idx = len(s) - 1
    for idx in range(len_s - 1, -1, -1):
        symbol = codes.get(s[idx])
        if symbol is None:
            s[new_idx] = s[idx]
            new_idx -= 1
        else:
            size = len(symbol)
            start = new_idx - size + 1
            end = new_idx + 1
            s[start:end] = symbol
            new_idx -= size
    return s


print(''.join(urlify(string_array, len(url))))
