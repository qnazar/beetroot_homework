"""Write a decorator that takes a list of stop words and replaces them with * inside the decorated function"""


def stop_words(words: list):
    def replace_words(func):
        def wrapper(*args):
            to_check, end = func(*args).rstrip("!").split(), func(*args)[-1]
            return ' '.join([word if word not in words else '*' for word in to_check]) + end
        return wrapper
    return replace_words


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('Steve'))
assert create_slogan('Steve') == "Steve drinks * in his brand new *!"
