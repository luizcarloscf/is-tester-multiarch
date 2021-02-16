from setuptools import setup, find_packages


def get_requirements(req_file="requirements.txt"):
    lines = [line.strip() for line in open(req_file)]
    return [line for line in lines if line]


setup(
    name='is_tester_multiarch',
    version='0.0.1',
    description='',
    url='http://github.com/luizcarloscf/is-tester-multiarch',
    author='luizcarloscf',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'is-tester-multiarch-rpc=is_tester_multiarch.rpc:main',
        ],
    },
    zip_safe=False,
    install_requires=[
        "is-msgs==1.1.10",
        "is-wire==1.2.0",
        "opencensus-ext-zipkin==0.2.1",
        "vine==1.3.0",
    ],
)
