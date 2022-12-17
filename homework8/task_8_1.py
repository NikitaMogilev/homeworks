def text_up(func):
    def wrap(*args):
        res = func(*args).upper()
        return res
    return wrap


@text_up
def get_text(*words):
    text = ' '.join(words)
    return text


text = get_text('Hello', 'World', 'Hi', 'dude')
print(text)
