import cx_Freeze

executables = [cx_Freeze.Executable('amoide.py')]

cx_Freeze.setup(
    name="Amoide Adventure",
    options={'build_exe': {'packages':['pygame'],
    'include_files': ['assets','sounds','fontes','emails.txt','__pycache__']}},
    executables = executables
)