# -*- mode: python -*-

block_cipher = None


a = Analysis(['uioscraper.py'],
             pathex=['/home/terje/Documents/projects/uio-scraper/'],
             binaries=[],
             datas=[],
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
          name='uioscraper',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )