# File: setup.py


from setuptools import setup, find_packages


requirements = [

]

setup(
    name="DNN",
    version="0.1",
    description="DNN",
    author="DV",
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    # entry_points={
    #     "console_scripts": [
    #         "tscrape = tscrape.train.gui:run",
    #     ]
    # },
)
