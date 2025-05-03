"""Legacy build script."""

from setuptools import setup  # pyright: ignore[reportMissingModuleSource]

install_requires = []

tests_require = ["pytest", "pytest-cov"]

_ = setup(
    name="ga_tests",
    version="0.0.1",
    description="Test GitHub Actions",
    platforms="any",
    license="MIT",
    tests_require=tests_require,
    install_requires=install_requires,
    extras_require={"tests": tests_require},
)
