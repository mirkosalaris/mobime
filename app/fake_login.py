__all__ = ["login_user", "logout_user", "authenticated"]

_user = ""


def login_user():
    global _user
    _user = "Giovanni"


def logout_user():
    global _user
    _user = ""


def authenticated():
    global _user
    return len(_user) > 0
