class text_up_decorator:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        res = self._func(*args, ).upper()
        return res


@text_up_decorator
def get_text(*words):
    text = ' '.join(words)
    return text


text = get_text('Hello', 'World', 'Hi', 'dude')
print(text)
