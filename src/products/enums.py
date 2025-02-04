from django.db import models


class ShippingType(models.enums.Choices):
    FULL = 'full'
    NORMAL = 'normal'
    

class InstallmentOption(models.enums.Choices):
    ONCE = '1x'
    TWICE = '2x'
    THREE_TIMES = '3x'
    FOUR_TIMES = '4x'
    FIVE_TIMES = '5x'
    SIX_TIMES = '6x'
    SEVEN_TIMES = '7x'
    EIGHT_TIMES = '8x'
    NINE_TIMES = '9x'
    TEN_TIMES = '10x'
    ELEVEN_TIMES = '11x'
    TWELVE_TIMES = '12x'
    ABOVE_12_TIMES = '+12x'

