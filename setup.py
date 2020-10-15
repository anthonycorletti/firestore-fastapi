from setuptools import setup

setup(name='firestore-fastapi',
      python_requires='>=3.8',
      author='Anthony Corletti',
      author_email='anthcor@gmail.com',
      url='https://github.com/anthcor/firestore-fastapi',
      license='MIT',
      zip_safe=True,
      install_requires=[
          'fastapi==0.61.1',
          'gunicorn==20.0.4',
          'uvicorn==0.12.1',
          'requests==2.24.0',
          'uvloop==0.14.0',
          'httptools==0.1.1',
          "google-cloud-firestore==1.9.0",
      ])
