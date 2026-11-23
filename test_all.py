import app
import login_utils

db = app.loadDB()

def test_real_un():
    assert login_utils.verify_un(db,"gunnar")

def test_fake_un():
    assert False==login_utils.verify_un(db,"gun")

def test_real_pw():
    assert login_utils.verify_pw(db,"admin","admin")

def test_fake_pw():
    assert False==login_utils.verify_pw(db,"admin","admina")
