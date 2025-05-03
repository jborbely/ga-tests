"""Legacy build script."""

from __future__ import annotations

from setuptools import setup  # type: ignore[import-untyped] # pyright: ignore[reportMissingModuleSource]

install_requires: list[str] = []

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
