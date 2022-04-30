from distutils.core import setup

setup(
    name="SlowLRS",
    py_modules=["slowLRS"],
    entry_points={"console_scripts": ["slowLRS=slowLRS:main"]},
    version="0.2.3",
    description="É uma ferramente de negação de serviço de baixa banda larga. Feito em Python.",
    author="MazumiYuki/LXrdKnowkill",
    author_email="MazumiKroto@gmail.com",
    url="hhttps://github.com/LXrdKnowkill/EmpyryanLXrd-SlowLRS",
    keywords=["dos", "http", "SlowLRS"],
    license="MIT",
)
