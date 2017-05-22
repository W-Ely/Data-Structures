"""Setup file."""
from setuptools import setup


setup(
    name='data_structures',
    description="""This is a collection of
multiple classic data structure implementations""",
    version='0.1',
    author="Casey and Ely",
    license='MIT',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'testing': ['pytest', 'pytest-cov']}
)
