import jamo
from hangul_jamo import decompose_syllable, compose_jamo_characters
from pruebas_present import conjugate_present


def conjugate_past(stem):
    # stem = conjugate_present(stem)[0][0:-1]
    formal = ''
    casual = ''

    if stem[-1] == '하':
        casual = stem[:-1] + '했어요'

    # if decompose_syllable(stem[-1])[1] == 'ㅏ' or decompose_syllable(stem[-1])[1] == 'ㅗ':
    #     casual = stem + jamo.hcj2j("ㅆ", "tail") + '어요'
    #
    # # if decompose_syllable(stem[-1])[1] =! ('ㅏ' or 'ㅗ') or decompose_syllable(stem[-1])[1] == 'ㅘ':
    # #     casual = stem + jamo.hcj2j("ㅆ", "tail") + '어요'
    #
    # if decompose_syllable(stem[-1])[1] == 'ㅓ' and decompose_syllable(stem[-1])[2] is None:
    #     casual = stem + jamo.hcj2j("ㅆ", "tail") + '어요'

    return casual


print(conjugate_past('가'))
print(conjugate_past('서'))
print(conjugate_past('만나'))

print(conjugate_past('보'))
print(conjugate_past('오'))

print(conjugate_past('먹'))
print(conjugate_past('재미있'))

print(conjugate_past('기다리'))
print(conjugate_past('마시'))

print(conjugate_past('아프'))
print(conjugate_past('쓰'))

print(conjugate_past('두'))

print(conjugate_past('쉽'))
print(conjugate_past('돕'))
print(conjugate_past('곱'))

print(conjugate_past('하'))
print(conjugate_past('청소하'))
print(conjugate_past('공부하'))
