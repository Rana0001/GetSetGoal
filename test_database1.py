
from database1 import *
import pytest


def test_insert():
    first_name = "Prashant"
    last_name = "Magar"
    gender = "Male"
    query = f"Insert into tbl_user(first_name,last_name,gender) values ('{first_name}','{last_name}','{gender}')"
    mydb = insert(query)

    assert mydb == 1