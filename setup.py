from setuptools import setup, find_packages

setup(
    name='chain_llm',
    version='0.0.1',
    packages=find_packages(),
    test_suite='tests',
    tests_require=[
        'unittest',
    ],
    author='awongh',
    author_email='akira@awongh.com',
    description='LLM Chaining Library',
    url='https://github.com/awongh/chain_llm',
    license='MIT',
)
