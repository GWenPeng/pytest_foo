from setuptools import setup
setup(
    name="pytest_foo",
    packages=["pytest_foo"],
    version="0.2.0",
    entry_points={
        "pytest11":["pytest_foo = pytest_foo.plugin"] #pytest11 入口
    },
    classifilers=["Framework :: Pytest"],
    install_requires=[
        'pytest','pytest-metadata'
    ],
)

#安装 pip install .