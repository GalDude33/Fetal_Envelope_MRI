from functools import partial

from .fetal_net import fetal_envelope_model
from .fetal_net_skip import fetal_origin_model
from .fetal_net_skip2 import fetal_origin2_model
from .fetal_net_skip3 import fetal_origin3_model

from .unet.unet import unet_model_2d
from .unet.isensee import isensee2017_model

from .unet3d.unet import unet_model_3d
from .unet3d.isensee2017 import isensee2017_model_3d

from .norm.NormNet import norm_net_model
from .unet.isensee_dis import isensee2017_model as dis_net
from .unet.isensee_style import isensee2017_model as dis_style_net

unet_model_2d_skip = partial(unet_model_2d, skip_connections=True)