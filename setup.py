import os
from distutils.core import setup


setup(
    name='lipsum',
    version="0.0.1",
    description='Lipsum',
    long_description=open(os.path.join(os.path.dirname(__file__), "readme.md")).read(),
    url='',
    download_url='',
    packages=['lipsum'],
    license='WTFPL',
    author='roundar',
    author_email='roundar.github@gmail.com',
    include_package_data=True,
    zip_safe=False,
    keywords=['lorem', 'ipsum', 'lorem ipsum', 'encoding'],
    entry_points={
        'console_scripts': [
            'lipsum = lipsum.__main__:main',
        ]
    },
)