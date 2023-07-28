from setuptools import setup

install_requires = [
    'numpy>=1.13.0',
    'scipy',
]
tests_require = [
    'pytest',
    'pytest-cov',
]

setup(
    name='ga_tests',
    version='0.0.1',
    description='Test GitHub Actions',
    platforms='any',
    license='MIT',
    tests_require=tests_require,
    install_requires=install_requires,
    extras_require={'tests': tests_require},
)
