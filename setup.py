from setuptools import setup, find_packages

setup(
    name='strictyaml-api',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'strictyaml=strictyaml_api.cli:main'
        ]
    },
    install_requires=[
        'pyyaml'
    ],
    author='ilPadrino',
    description='Strict, safe YAML format for APIs with CLI validation',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
