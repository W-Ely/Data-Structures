"""Setup file."""
from setuptools import setup


setup(
    name='data_structures',
    description="""This is a collection of
multiple classic data structure implementations""",
    version='0.1',
    author="Casey and Ely",
    license='MIT',
    py_modules=[
        'binheap', 'bbst', 'bst', 'deque', 'dll', 'graph',
        'linked_list', 'priority_queue', 'que_', 'stack', 'weighted_graph'
    ],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'testing': ['pytest', 'pytest-cov', 'tox']}
)
