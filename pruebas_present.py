import jamo
from hangul_jamo import decompose_syllable, compose_jamo_characters


def conjugate_present(stem):
    formal = ''
    casual = ''
    casual_present_exceptions = ['돕', '곱', '하']

    # Casual
    # Irregular verbs (ends with ㅂ)
    if decompose_syllable(stem[-1])[2] == 'ㅂ' and (stem not in casual_present_exceptions):
        for i in range(len(stem) - 1):
            casual = casual + stem[i]
        casual = casual + compose_jamo_characters(decompose_syllable(stem[-1])[0], decompose_syllable(stem[-1])[1], None) + '워요'
    # Exceptions in irregular verbs
    if (stem == '돕') or (stem == '곱'):
        for i in range(len(stem) - 1):
            casual = casual + stem[i]
        casual = casual + compose_jamo_characters(decompose_syllable(stem[-1])[0], decompose_syllable(stem[-1])[1],
                                                  None) + '와요'
    # If the verb's stem ends in ㅏ or ㅓ
    if (decompose_syllable(stem[-1])[1] == 'ㅏ' or decompose_syllable(stem[-1])[1] == 'ㅓ') and \
            decompose_syllable(stem[-1])[2] is None and (stem not in casual_present_exceptions):
        casual = stem + '요'
    # Exception: 하 to 해
    if stem[-1] == '하':
        casual = stem[:-1] + '해요'
    # If the verb's stem last vowel is ㅏ or ㅗ
    elif (decompose_syllable(stem[-1])[1] == 'ㅏ' or decompose_syllable(stem[-1])[1] == 'ㅗ') and \
            (decompose_syllable(stem[-1])[2] is not None and decompose_syllable(stem[-1])[2] != 'ㅂ'):
        casual = stem + '아요'
    # If the verb's stem ends in ㅗ
    elif decompose_syllable(stem[-1])[1] == 'ㅗ' and decompose_syllable(stem[-1])[2] is None:
        for i in range(len(stem) - 1):
            casual = casual + stem[i]
        casual = casual + compose_jamo_characters(decompose_syllable(stem[-1])[0], 'ㅘ', None) + '요'
    # If the verb's stem last vowel is NOT ㅏ or ㅗ
    elif (decompose_syllable(stem[-1])[1] != 'ㅏ' and decompose_syllable(stem[-1])[1] != 'ㅗ') and \
            (decompose_syllable(stem[-1])[2] is not None and decompose_syllable(stem[-1])[2] != 'ㅂ'):
        casual = stem + '어요'
    # If the verb's stem ends in ㅜ
    elif decompose_syllable(stem[-1])[1] == 'ㅜ' and decompose_syllable(stem[-1])[2] is None:
        for i in range(len(stem) - 1):
            casual = casual + stem[i]
        casual = casual + compose_jamo_characters(decompose_syllable(stem[-1])[0], 'ㅝ', None) + '요'
    # If the verb's stem ends in ㅣ
    elif decompose_syllable(stem[-1])[1] == 'ㅣ' and decompose_syllable(stem[-1])[2] is None:
        for i in range(len(stem) - 1):
            casual = casual + stem[i]
        casual = casual + compose_jamo_characters(decompose_syllable(stem[-1])[0], 'ㅕ', None) + '요'

    # If the verb's stem ends in ㅡ
    if decompose_syllable(stem[-1])[1] == 'ㅡ':
        # If the verb's stem has more than 1 syllable, check the vowel of the second last syllable, if this is ㅏ or ㅗ,
        # we change the ㅡ of the last for a ㅏ
        if (len(stem) > 1) and (decompose_syllable(stem[-2])[1] == 'ㅏ' or decompose_syllable(stem[-2])[1] == 'ㅗ'):
            for i in range(len(stem) - 1):
                casual = casual + stem[i]
            casual = casual + compose_jamo_characters(decompose_syllable(stem[-1])[0], 'ㅏ', None) + '요'
        # If the verb's stem has only one syllable (with ㅡ as vowel), we change the vowel to ㅓ
        else:
            for i in range(len(stem) - 1):
                casual = casual + stem[i]
            casual = casual + compose_jamo_characters(decompose_syllable(stem[-1])[0], 'ㅓ', None) + '요'

    # Formal
    # If the verb's stem ends in a consonant or ㄹ
    if decompose_syllable(stem[-1])[2] == 'ㄹ':
        for i in range(len(stem)-1):
            formal = formal + stem[i]
        stem_last_jamos = decompose_syllable(stem[-1])
        formal = formal + compose_jamo_characters(stem_last_jamos[0], stem_last_jamos[1], 'ㅂ') + '니다'
    elif (decompose_syllable(stem[-1])[2] != 'ㄹ') and (decompose_syllable(stem[-1])[2] is not None):
        formal = stem + '습니다'
    # If the verb's stem ends in a vowel
    else:
        formal = stem + jamo.hcj2j("ㅂ", "tail") + '니다'

    return casual, formal


# Real case proofs
print(conjugate_present('가'))
print(conjugate_present('서'))
print(conjugate_present('만나'))

print(conjugate_present('보'))
print(conjugate_present('오'))

print(conjugate_present('먹'))
print(conjugate_present('재미있'))

print(conjugate_present('기다리'))
print(conjugate_present('마시'))

print(conjugate_present('아프'))
print(conjugate_present('쓰'))

print(conjugate_present('두'))

print(conjugate_present('쉽'))
print(conjugate_present('돕'))
print(conjugate_present('곱'))

print(conjugate_present('하'))

print(conjugate_present('청소하'))
print(conjugate_present('공부하'))


