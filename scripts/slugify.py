import re


def slugify_unicode(value, separator, encoding='utf8'):
    
    value = value.encode(encoding, 'ignore')
    value = re.sub(r'[^\w\s-]', '', value.decode(encoding)).strip().lower()
    return re.sub(r'[%s\s]+' % separator, separator, value)


__all__ = \
[
    'slugify_unicode',
]
