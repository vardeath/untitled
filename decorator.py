def args_kwargs_example(first_arg, second_arg, *args, **kwargs):
    print("first_arg:", first_arg)
    print("second_arg:", second_arg)
    print("args:", args)
    print("kwargs:", kwargs)


params = ("aaa", "bbb")
k_params = {"param1": "some_param", "param2": 42}
args_kwargs_example("111", 123, 456, *params, name="NaMe", **k_params)
