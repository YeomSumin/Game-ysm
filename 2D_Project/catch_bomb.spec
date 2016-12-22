# -*- mode: python -*-

block_cipher = None


a = Analysis(['catch_bomb.py'],
             pathex=['C:\\2DGP\\GitHub\\Game-ysm\\2D_Project'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='catch_bomb',
          debug=False,
          strip=False,
          upx=True,
          console=True )
