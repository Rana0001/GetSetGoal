import database1
import pytest

def test_login():
    username = "Rana0001"
    password = "pass1234"
    answer = database1.login(username,password)
    assert answer == "Pass"

def test_login1():
    username = "Magar0001"
    password = "pass1234"
    answer = database1.login(username,password)
    assert answer == "Pass"

def test_register():
    first_name = "Subina"
    last_name = "Khadka"
    email = "Subinak"
    password = "123456"
    gender = "Female"
    contact_no = "9811775566"
    answer = database1.register(first_name,last_name,email,password,gender,contact_no)
    assert answer == None

def test_delete():
    email = "Rana0001"
    answer = database1.delete(email)
    assert answer == None

def test_update():
    first_name = "Bhupraj"
    last_name = "Tamang"
    email = "Rana0001"
    answer = database1.update(first_name,last_name,email)
    assert answer == None