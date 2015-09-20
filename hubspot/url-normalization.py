def checkio(url):
    import re
    url = url.lower()
    es_list = [i.upper() for i in re.findall('%..?',url)]
    str_list = re.split('%..?',url)
    url = ''
    for idx in range(len(es_list)):
        ch = int(es_list[idx][1:], base = 16)
        if int('41', base = 16) <= ch <= int('5A', base = 16)\
        or int('61', base = 16) <= ch <= int('7A', base = 16)\
        or int('30', base = 16) <= ch <= int('39', base = 16)\
        or ch in [int(x, base = 16) for x in ['2D', '2E', '5F', '7E']]:
            es_list[idx] = chr(ch)
        url = url + str_list[idx] + es_list[idx]
    url = url + str_list[-1]
    url = '/'.join(re.split(':80/',url))
    url = ''.join(re.split(':80$',url))
    url = ''.join(re.split('/[0-9a-zA-Z]+/\.\.',url))
    url = ''.join(re.split('/\.',url))
    return url

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:80") == \
        "http://www.checkio.org", "4th rule"

    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')