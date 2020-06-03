from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-aaron-ds15", # the name that you will install via pip
    version="2.0",
    author="Aaron Huizenga",
    author_email="aaron-huizenga@lambdastudents.com",
    description="Aaron's first ever local project!",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/nusc2016/lambdata-ds15",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)