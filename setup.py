from setuptools import find_packages, setup

setup(
    name='python-laravel-queue',
    packages=find_packages(
        where='src',
        include=['python_laravel_queue*'],
    ),
    include_package_data=True,
    version='0.0.1b3',
    description='Sync Laravel queue with Python.',
    author='Sinan Bekar',
    license='MIT',
)
