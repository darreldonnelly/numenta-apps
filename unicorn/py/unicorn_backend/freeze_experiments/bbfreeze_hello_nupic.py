from bbfreeze import Freezer
f = Freezer("model_runner", includes=("nupic",))
f.addScript("model_runner.py")        # If there are multiple source files, just repeat this to add more
f() # starts the freezing process
