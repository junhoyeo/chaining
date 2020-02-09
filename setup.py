import setuptools

with open('README.md', 'r') as file_handler:
    long_description = file_handler.read()

setuptools.setup(
    name='chaining',
    packages=['chaining'],
    version='0.0.2',
    license='MIT',
    description=
    'Package that implements functional chaining in Python, which behaves like JavaScript',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Junho Yeo',
    author_email='hanaro0704@gmail.com',
    url='https://github.com/junhoyeo/chaining',
    download_url='https://github.com/junhoyeo/chaining/archive/v_0.0.2.tar.gz',
    keywords=[
        'functional',
        'chaining',
    ],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
