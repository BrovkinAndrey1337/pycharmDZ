import pytest
from src.decorators import log

@log()
def successful_function(x):
    return x * 2

@log()
def function_with_exception(x):
    return x / 0

def test_successful_function(capsys):
    result = successful_function(5)
    captured = capsys.readouterr()
    assert result == 10
    assert "successful_function ok" in captured.out

def test_function_with_exception(capsys):
    with pytest.raises(ZeroDivisionError):
        result = function_with_exception(5)
        captured = capsys.readouterr()
        assert result is None
        assert "function_with_exception error: ZeroDivisionError. Inputs: (5,), {}" in captured.out