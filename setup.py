#!/usr/bin/env python
from pip.req import parse_requirements
from setuptools import setup


def get_requirements(filename):
    try:
        from pip.download import PipSession

        session = PipSession()
    except ImportError:
        session = None

    reqs = parse_requirements(filename, session=session)
    return [str(r.req) for r in reqs]


setup_args = dict(
    name='secureiowa',
    version="0.0.1",
    author='Jeffrey Melvin',
    install_requires=get_requirements('requirements.txt'),
    packages=[],
    package_dir={},
    zip_safe=False,
    include_package_data=True,
)

if __name__ == '__main__':
    setup(**setup_args)
