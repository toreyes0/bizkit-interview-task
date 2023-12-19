from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    output = []
    for key in args.keys():
        for user_data in USERS:
            if (key == 'id' and args[key] == user_data[key]) or \
               (key in ['name', 'occupation'] and args[key] in user_data[key]) or \
               (key == 'age' and int(args[key]) >= int(user_data[key]) - 1  and int(args[key]) <= int(user_data[key]) + 1):
                output.append(user_data)
 
    return output
