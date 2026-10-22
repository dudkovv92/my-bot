from collections import ChainMap

defaults = {"theme": "dark", "lang": "ru"}
user_settings = {"theme": "light"}

settings = ChainMap(user_settings, defaults)

print(settings["theme"])  # из user_settings
print(settings["lang"])   # из defaults
print(settings["theme"])  # из user_settings (первый)