def check_if_user_exists(user_st, username, email):
    """check if the username or email has already been used"""

    for item in user_st:
        if item[1] == username:
            return 'Sorry, This username has already been taken'
        if item[2] == email:
            return 'Sorry, This email is already in use'