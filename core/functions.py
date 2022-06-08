def is_english(value):
    try:
        value.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def checkbox_to_bool(value):
    if value == 'on': return True
    else: return False