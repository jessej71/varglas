from distutils.core import setup

setup( name        ='VarGlaS',
       version     ='1.0',
       description ='Variational Glacier Simulator (VarGlaS)',
       author      ='Douglas Brinkerhoff, Jesse Johnson, Evan Cummings',
       url         ='https://github.com/pf4d/varglas',
       packages    =['varglas', 
                     'varglas.plot', 
                     'varglas.mesh', 
                     'varglas.data',
                     'varglas.data.greenland',
                     'varglas.data.antarctica',
                     'tifffile'],
       package_dir ={'varglas'                 : 'src',
                     'varglas.plot'            : 'src/plot', 
                     'varglas.mesh'            : 'src/mesh', 
                     'varglas.data'            : 'src/data',
                     'varglas.data.greenland'  : 'src/data/greenland',
                     'varglas.data.antarctica' : 'src/data/antarctica',
                     'tifffile'                : 'src/ext_scripts'}
     )
