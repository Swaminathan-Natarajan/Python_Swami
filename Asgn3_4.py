def default_param(Name="Swami", Age=None):
    if Age is not None:
        print(f"My Name is {Name} and my age is {Age}")
    else:
        print(f"My Name is {Name}")

default_param()
default_param("Ram", 30)
default_param("Ganesh")


