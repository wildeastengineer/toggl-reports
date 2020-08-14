import os


def get_variable(var_name):
    value = os.environ.get(var_name)

    if not value:
        print("Variable \'" + var_name + "\" was not found in environment variables.")
        value = input("Enter \"" + var_name + "\" value:")
        os.environ[var_name] = value

    return value


def get_variables():
    toggl_api_key = get_variable("TOGGL_API_KEY")

    return {"toggl_api_key": toggl_api_key}
