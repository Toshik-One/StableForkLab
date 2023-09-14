#blasphemy = "stable-diffusion-webui"
StableForkLab = "StableForkLab"
contrlnet = "sd-webui-controlnet"
import os
if os.path.exists("/content/gdrive"):
  storage_path = f"/content/gdrive/{mainpth}"
else:
  storage_path = "/content"
