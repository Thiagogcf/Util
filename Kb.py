import glob
import os
import shutil
import patoolib
local = os.getcwd()
print(local)
local = r'D:\KB\GX9'
rede = r'\\172.28.181.212\produtos\VERSAOSQLSERVER\KB\154\*.rar'
list_of_files = glob.glob(rede) # * means all if need specific format then *.cs v
print(list_of_files)
for x in list_of_files:
    x.replace('\\\\','\\')
latest_file = max((list_of_files), key=os.path.getctime)
print(os.path.basename(latest_file))
print(latest_file)
print("baixando Kb.rar")
shutil.copyfile(latest_file, local+'\\'+os.path.basename(latest_file))
print("Deszipando Kb")
versao = os.path.splitext(os.path.basename(latest_file))[0]
kb = local+'//'+versao
isExist = os.path.exists(kb)
if not isExist:
    os.makedirs(kb)
patoolib.extract_archive(kb+'.rar', outdir=kb)
os.remove(kb+'.rar')
print('deszipando arquivos avulsos')
patoolib.extract_archive(kb+'\\DATA004.rar', outdir=kb)
os.remove(kb+'\\DATA004.rar')
patoolib.extract_archive(kb+'\\DATA005.rar', outdir=kb)
os.remove(kb+'\\DATA005.rar')
patoolib.extract_archive(kb+'\\GXSPC002.rar', outdir=kb)
os.remove(kb+'\\GXSPC002.rar')
patoolib.extract_archive(kb+'\\GXSPC003.rar', outdir=kb)
os.remove(kb+'\\GXSPC003.rar')


print('kb copiada')