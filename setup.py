from setuptools import setup, find_packages

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
        "googleapis-common-proto==1.52.0",
        "vine==1.3.0",
    ],
)
