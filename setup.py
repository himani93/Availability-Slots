from setuptools import (
    setup,
    find_packages,
)


setup(name='Availability Slots',
      version='0.1',
      description='Availability Slots - Given a weekly schedule provide available slots from a given time',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='healthifyme availability slots',
      author='Himani Agrawal',
      author_email='himani93@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
      ],
      tests_require=['pytest'],
      setup_require=['pytest-runner'],
      include_package_data=True,
      entry_points={
          'console_scripts': ['available-slots=available_slots.main:main'],
      },
      zip_safe=False)
