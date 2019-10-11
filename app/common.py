from app.fake_login import authenticated


def common_variables():
    var_dict = {}
    var_dict["authenticated"] = authenticated()
    var_dict["username"] = "Giovanni"

    return var_dict