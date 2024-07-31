from .gans import RCGAN, RCWGAN, TimeGAN, CWGAN
from .gmmn import GMMN
from .sigcwgan import SigCWGAN

ALGOS = dict(SigCWGAN=SigCWGAN, TimeGAN=TimeGAN, RCGAN=RCGAN, GMMN=GMMN, RCWGAN=RCWGAN, CWGAN=CWGAN)
