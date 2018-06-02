import re


def unicode(s):
    """No-op."""
    return s


def safe_filename(s, max_length=255):
    """Sanitize a string making it safe to use as a filename.

    This function was based off the limitations outlined here:
    https://en.wikipedia.org/wiki/Filename.

    :param str s:
        A string to make safe for use as a file name.
    :param int max_length:
        The maximum filename character length.
    :rtype: str
    :returns:
        A sanitized string.
    """
    # Characters in range 0-31 (0x00-0x1F) are not allowed in ntfs filenames.
    ntfs_chrs = [chr(i) for i in range(0, 31)]
    chrs = [
        '\"', '\#', '\$', '\%', '\'', '\*', '\,', '\.', '\/', '\:', '"',
        '\;', '\<', '\>', '\?', '\\', '\^', '\|', '\~', '\\\\',
    ]
    pattern = '|'.join(ntfs_chrs + chrs)
    regex = re.compile(pattern, re.UNICODE)
    filename = regex.sub('', s)
    return unicode(filename[:max_length].rsplit(' ', 0)[0])
