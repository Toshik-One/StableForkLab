import os
import requests
import time
import ipywidgets as widgets
from IPython.utils import capture
from IPython.display import clear_output
from tqdm import tqdm

print('[1;32mУстановка/Обновление AUTOMATIC1111 repo...')

with capture.capture_output() as cap:
  def inf(msg, style, wdth): inf = widgets.Button(description=msg, disabled=True, button_style=style, layout=widgets.Layout(min_width=wdth));display(inf)
  fgitclone = "git clone --depth 1"
  %mkdir -p $storage_path/sd
  %cd $storage_path/sd
  #!git clone -q --branch master https://github.com/AUTOMATIC1111/$blasphemy
  #!git clone https://github.com/AUTOMATIC1111/$blasphemy.git --branch v1.5.2
  !git clone -b v1.6.0 https://github.com/AUTOMATIC1111/$blasphemy
  !mkdir -p $storage_path/sd/$blasphemy/cache/
  os.environ['TRANSFORMERS_CACHE']=f"{storage_path}/sd/"+blasphemy+"/cache"
  os.environ['TORCH_HOME'] = f"{storage_path}/sd/"+blasphemy+"/cache"

with capture.capture_output() as cap:
  %cd $storage_path/sd/$blasphemy/
  !git reset --hard
  !git checkout v1.6.0
  time.sleep(1)
  !rm webui.sh
  !git pull
clear_output()

print('[1;32mУстановка requirements...')

with capture.capture_output() as cap:
  %cd /content/
  !wget -q -i https://raw.githubusercontent.com/TheLastBen/fast-stable-diffusion/main/Dependencies/A1111.txt
  !dpkg -i *.deb
  if not os.path.exists(''+storage_path+'/sd/stablediffusion'):
    !tar -C $storage_path --zstd -xf sd_mrep.tar.zst
  !tar -C / --zstd -xf gcolabdeps.tar.zst
  !rm *.deb | rm *.zst | rm *.txt

  if not os.path.exists(''+storage_path+'/sd/stablediffusion/libtcmalloc/libtcmalloc_minimal.so.4.3.0'):
    %env CXXFLAGS=-std=c++14
    !wget -q https://github.com/gperftools/gperftools/releases/download/gperftools-2.5/gperftools-2.5.tar.gz && tar zxf gperftools-2.5.tar.gz && mv gperftools-2.5 gperftools
    !wget -q https://github.com/TheLastBen/fast-stable-diffusion/raw/main/AUTOMATIC1111_files/Patch
    %cd /content/gperftools
    !patch -p1 < /content/Patch
    !./configure --enable-minimal --enable-libunwind --enable-frame-pointers --enable-dynamic-sized-delete-support --enable-sized-delete --enable-emergency-malloc; make -j4
    !mkdir -p $storage_path/sd/stablediffusion/libtcmalloc && cp .libs/libtcmalloc*.so* $storage_path/sd/stablediffusion/libtcmalloc
    %env LD_PRELOAD=$storage_path/sd/stablediffusion/libtcmalloc/libtcmalloc_minimal.so.4.3.0
    %cd /content
    !rm *.tar.gz Patch && rm -r /content/gperftools
  else:
    %env LD_PRELOAD=$storage_path/sd/stablediffusion/libtcmalloc/libtcmalloc_minimal.so.4.3.0

  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
  os.environ['PYTHONWARNINGS'] = 'ignore'
  !sed -i 's@text = _formatwarnmsg(msg)@text =\"\"@g' /usr/lib/python3.10/warnings.py

clear_output()

if Path_to_MODEL == "":
    model = ""+storage_path+"/sd/"+blasphemy+"/models/Stable-diffusion"
else:
    found = False

    while not found:
        if Path_to_MODEL.endswith('.ckpt') or Path_to_MODEL.endswith('.safetensors'):
            if os.path.exists(str(Path_to_MODEL)):
                inf('\u2714 Путь к обученной/ым модели/ям указан.','success', '285px')
                found = True

        else:
            for root, dirs, files in os.walk(Path_to_MODEL):
                for file in files:
                    if file.endswith('.ckpt') or file.endswith('.safetensors'):
                        inf('\u2714 Путь к обученной/ым модели/ям указан.','success', '285px')
                        found = True
                        break
                else:
                    continue
                break
            else:
                inf('\u2718 Неверный путь: Указанный путь не содержит файлы .ckpt или .safetensors','danger', '490px')
                print("Используйте проводник файлов Colab, чтобы скопировать путь :")
                Path_to_MODEL=input(prompt='', )

        clear_output(wait=True)
    model=Path_to_MODEL
inf('\u2714 Готово','success', '50px')
