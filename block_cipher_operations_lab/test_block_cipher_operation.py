#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bitstring import BitArray
import inspect, sys
from terminaltables import AsciiTable


# In[ ]:


def test_double_key(double_key):
    input_block = BitArray('0b0100000111111010010101100001010101111011111001100100111011001011')
    K1 = BitArray('0b0111010101101111110011100110110111110100000110010001000001000000')
    K2 = BitArray('0b1001111100100111000110001011111101000101011100010000110110001111')
    keys = {'K1': K1, 'K2': K2}
    cipher_block = double_key(input_block, keys, mode='E')
    decoded_block = double_key(cipher_block, keys, mode='D')
    return input_block == decoded_block


# In[ ]:


def test_triple_cipher(triple_cipher):
    input_block = BitArray('0b0100000111111010010101100001010101111011111001100100111011001011')
    K1 = BitArray('0b0111010101101111110011100110110111110100000110010001000001000000')
    K2 = BitArray('0b1001111100100111000110001011111101000101011100010000110110001111')
    K3 = BitArray('0b1111011000010111010001010110100010110001000010100110110011110000')
    keys = {'K1': K1, 'K2': K2, 'K3': K3}
    cipher_block = triple_cipher(input_block, keys, mode='E')
    decoded_block = triple_cipher(cipher_block, keys, mode='D')
    return input_block == decoded_block


# In[ ]:


def test_ecb_mode(ecb_mode, triple_cipher):
    input_blocks = []
    input_blocks.append(BitArray('0b0100000111111010010101100001010101111011111001100100111011001011'))
    input_blocks.append(BitArray('0b0100000100011010010001001001111001010000000111100011101010101011'))
    input_blocks.append(BitArray('0b1001111101110000111100001001101011011001001010100100010110011011'))
    input_blocks.append(BitArray('0b0000110111100101100110111000011101011101110101000011111111001000'))
    input_blocks.append(BitArray('0b0010000010010101110001001111010001111101100001110100110011110010'))
    input_blocks.append(BitArray('0b0110100111100000011011010100101010111111100011100011011111010001'))

    K1 = BitArray('0b0111010101101111110011100110110111110100000110010001000001000000')
    K2 = BitArray('0b1001111100100111000110001011111101000101011100010000110110001111')
    K3 = BitArray('0b1111011000010111010001010110100010110001000010100110110011110000')
    keys = {'K1': K1, 'K2': K2, 'K3': K3}
    cipher_blocks = ecb_mode(input_blocks, keys, cipher=triple_cipher, mode='E')
    decoded_blocks = ecb_mode(cipher_blocks, keys, cipher=triple_cipher, mode='D')
    counter = 0
    for input_block, decoded_block in zip(input_blocks, decoded_blocks):
        if input_block == decoded_block:
            counter +=1
    return counter == len(input_blocks)
        


# In[ ]:


def test_cbc_mode_unit(cbc_mode_unit, triple_cipher):
    input_block = BitArray('0b0100000111111010010101100001010101111011111001100100111011001011')
    K1 = BitArray('0b0111010101101111110011100110110111110100000110010001000001000000')
    K2 = BitArray('0b1001111100100111000110001011111101000101011100010000110110001111')
    K3 = BitArray('0b1111011000010111010001010110100010110001000010100110110011110000')
    IV = BitArray('0b0111001100100001101001001110110101110011101010001100000111111011')
    keys = {'K1': K1, 'K2': K2, 'K3': K3, 'IV': IV}
    cipher_block = cbc_mode_unit(input_block, keys, cipher=triple_cipher, mode='E')
    decoded_block = cbc_mode_unit(cipher_block, keys, cipher=triple_cipher, mode='D')
    return input_block == decoded_block


# In[ ]:


def test_cbc_mode(cbc_mode, triple_cipher):
    input_blocks = []
    input_blocks.append(BitArray('0b0100000111111010010101100001010101111011111001100100111011001011'))
    input_blocks.append(BitArray('0b0100000100011010010001001001111001010000000111100011101010101011'))
    input_blocks.append(BitArray('0b1001111101110000111100001001101011011001001010100100010110011011'))
    input_blocks.append(BitArray('0b0000110111100101100110111000011101011101110101000011111111001000'))
    input_blocks.append(BitArray('0b0010000010010101110001001111010001111101100001110100110011110010'))
    input_blocks.append(BitArray('0b0110100111100000011011010100101010111111100011100011011111010001'))

    K1 = BitArray('0b0111010101101111110011100110110111110100000110010001000001000000')
    K2 = BitArray('0b1001111100100111000110001011111101000101011100010000110110001111')
    K3 = BitArray('0b1111011000010111010001010110100010110001000010100110110011110000')
    IV = BitArray('0b0111001100100001101001001110110101110011101010001100000111111011')
    keys = {'K1': K1, 'K2': K2, 'K3': K3, 'IV': IV}

    cipher_blocks = cbc_mode(input_blocks, keys, cipher=triple_cipher, mode='E')
    keys = {'K1': K1, 'K2': K2, 'K3': K3, 'IV': IV}
    decoded_blocks = cbc_mode(cipher_blocks, keys, cipher=triple_cipher, mode='D')
    counter = 0
    for input_block, decoded_block in zip(input_blocks, decoded_blocks):
        if input_block == decoded_block:
            counter +=1

    return counter == len(input_blocks)


# In[ ]:


def get_module_functions(module):
    ret = {}
    for name,obj in inspect.getmembers(module):
        if (inspect.isfunction(obj) and not name.startswith('test')):
            ret[name] = obj
    return ret


# In[ ]:


def evaluate(exercise_functions):
    test_functions = {}
    for name,obj in inspect.getmembers(sys.modules[__name__]):
        if (inspect.isfunction(obj) and name.startswith('test')):
            test_functions[name] = obj
    
    grade_summary = [
        ['Index','Exercise', 'Passed', 'Grade']]
    exam_grade = 0
    for index,fun in enumerate(test_functions.keys()):
        fun_sig = inspect.signature(eval(fun))
        evaluate_args = []
        for fun_arg in fun_sig.parameters:
            evaluate_args.append(exercise_functions[fun_arg])
            
        try:
            flag = test_functions[fun](*tuple(evaluate_args))
        except:
            flag = 0
            
        grade_summary.append([str(index), fun.replace('test_',''), str(flag), str(flag * 10)])
        exam_grade += int(flag * 10)
  
    grade_table = AsciiTable(grade_summary)
    print(grade_table.table)
    print("Exam Grade: {0:.2f}".format((exam_grade/(len(test_functions) * 10)) * 100))
    

