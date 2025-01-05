def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            error_occured = False
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                result = None
                error_occured = True
                error = e
            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)
            if error_occured is True:
                raise error
            return result

        return wrapper

    return decorator
