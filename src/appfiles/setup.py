from setuptools import setup
setup(
    app=["app.py"],
    options={'py2app':{'argv_emulation':True,'emulate_shell_environment':1}},
    setup_requires=["py2app"],
)
