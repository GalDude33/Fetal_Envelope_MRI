from functools import partial

from .fetal_net import fetal_envelope_model
from .fetal_net_skip import fetal_origin_model
from .fetal_net_skip2 import fetal_origin2_model
from .fetal_net_skip3 import fetal_origin3_model

from .unet.unet import unet_model_2d
from .unet.isensee import isensee2017_model

from .unet3d.unet import unet_model_3d
from .unet3d.isensee2017 import isensee2017_model_3d
#from .unet3d.isensee2017_2 import isensee2017_model_3d as isensee2017_2_model_3d

from .norm.NormNet import norm_net_model

from .discriminator.all_dis_2d import discriminator_image_2d
from .discriminator.all_dis_3d import discriminator_image_3d
