from setuptools import setup

setup(
    version="1.0.1",
    py_modules=["wifi"],
    requires=["git+https://github.com/burgrp/micropython-virtual-timer.git@v1.0.0"]
)