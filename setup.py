from setuptools import setup

setup(name="xplay",
      version="0.13",
      description="play any song from terminal",
      url="http://github.com/zuck007/xplay",
      author="Pradeep Khileri",
      author_email="pradeepchoudhary009@gmail.com",
      license="MIT",
      scripts=["./bin/xplay"],
      keywords='music song-tags metadata unix linux script cli-tool',
      install_requires=[
          "musicquery",
          "colorama",
      ],
      zip_safe=False)

