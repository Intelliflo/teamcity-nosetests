from nose.tools import *
from teamcitynosetests import *

def setup():
    pass

def teardown():
    pass

def test_escape_message_single_quote():
    assert_equal(escape_message("'"), "|'")

def test_escape_message_newline():
    assert_equal(escape_message("\n"), "|n")

def test_escape_message_carriagereturn():
    assert_equal(escape_message("\r"), "|r")

def test_escape_message_vbar():
    assert_equal(escape_message("|"), "||")

def test_escape_message_obrack():
    assert_equal(escape_message("["), "|[")

def test_escape_message_cbrack():
    assert_equal(escape_message("]"), "|]")

def test_escape_unicode_char():
    assert_equal(escape_message("\u0394"), "|0x0394")

def test_multiple_escapes():
    assert_equal(escape_message("[]|[']|[]"), "|[|]|||[|'|]|||[|]")

def test_non_escaped():
    assert_equal(escape_message("Quick brown fox!"), "Quick brown fox!")

