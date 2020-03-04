
from pathlib import Path
#from config import VCR_IMAGES_DIR, VCR_ANNOTS_DIR
import jsonlines as jsnl
import json
import tqdm
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

#matplotlib.use('agg')

import os

import warnings

#from models.eval_q2ar import answer_preds, rationale_preds

warnings.filterwarnings("ignore")

VCR_DIR = Path('../data/')
VCR_IMAGES = VCR_DIR / 'vcr1images'
val_file = Path('../data/') / 'val.jsonl'

val_annots = jsnl.Reader(open(val_file))
print('val_annots is', type(val_annots))

t1 = []
#for t in tqdm.tqdm_notebook(val_annots.iter()):
for t in val_annots.iter():
    t1.append(t)

image_id = 50
anno = t1[image_id]   #change the image

print('anno is', type(anno))
print(anno.keys())

#anno['objects']

### Import from File
from notebooks.visualizer import Visualizer
vis = Visualizer(VCR_DIR, anno)
img, mask_img, odct = vis.get_img(), vis.get_mask_ann_img(), vis.get_qar()
answer_name_list = ['0', '1', '2', '3']
answer_num_list = answer_preds[image_id]
#plt.barh(range(len(answer_num_list)), answer_num_list, tick_label = answer_name_list)
#plt.bar(range(len(answer_num_list)), answer_num_list, tick_label = answer_name_list)
plt.show()

rationale_name_list = ['0', '1', '2', '3']
rationale_num_list = rationale_preds[image_id]
plt.barh(range(len(rationale_num_list)), rationale_num_list, tick_label = rationale_name_list)

plt.show()


img.show()
mask_img.show()
print(odct)
#print(type(odct))
print(anno['question'])

