#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bitstring import BitArray
import inspect, sys
from terminaltables import AsciiTable


# In[6]:


def test_cfb_unit(cfb_unit):
    input_bits = BitArray('0b00111010')
    K = BitArray('0b1111100001101110011110000010110110001110101001010110100110111011')
    I = BitArray('0b1000100011001101100011101001101000001001111110101101111001000011')
    cipher_bits = cfb_unit(K, I, input_bits)
    decoded_bits = cfb_unit(K, I, cipher_bits)
    return decoded_bits == input_bits


# In[ ]:


def test_cfb(cfb):
    input_blocks = [
    BitArray('0b00100111'),
    BitArray('0b11000101'),
    BitArray('0b10100100'),
    BitArray('0b00011110'),
    BitArray('0b11110001'),
    BitArray('0b01110001'),
    BitArray('0b11000001'),
    BitArray('0b01001111'),
    BitArray('0b11000100'),
    BitArray('0b01101000')]

    K = BitArray('0b1111100001101110011110000010110110001110101001010110100110111011')
    IV = BitArray('0b1000100011001101100011101001101000001001111110101101111001000011')
    keys = {'K': K, 'IV': IV}

    cipher_blocks = cfb(input_blocks, keys, mode='E')
    decoded_blocks = cfb(cipher_blocks, keys, mode='D')

    counter = 0
    for input_bits, decoded_bits in zip(input_blocks, decoded_blocks):
        if input_bits == decoded_bits:
            counter +=1
    return counter == len(input_blocks)


# In[ ]:


def test_ofb(ofb):
    input_blocks = [BitArray('0b0111001011111100010100001111011010011001000010100110110000010100'),
    BitArray('0b0011000001011110010100001110110110110110101111010101011001010110'),
    BitArray('0b0110111011001111010010101100111111110010101110011110001011110000'),
    BitArray('0b0010000110001111100111001101001010011010101001111100010000000100'),
    BitArray('0b0110001111100011101011100011111000010011001100100001010110010011'),
    BitArray('0b0000000110111000111100000011001101000100010100001001111111001101'),
    BitArray('0b1010011001000111011100111000011101101011100000110011011001010010'),
    BitArray('0b0010100001111010101110001100010110110100101101000011000001100100'),
    BitArray('0b0110101100010001101100111000101011011101001111110101001110101101'),
    BitArray('0b1001101011110001100101001101011100111001101110011011001000100000')]

    K = BitArray('0b1111100001101110011110000010110110001110101001010110100110111011')
    IV = BitArray('0b1000100011001101100011101001101000001001111110101101111001000011')
    keys = {'K': K, 'NONCE': IV}

    cipher_blocks = ofb(input_blocks, keys)
    decoded_blocks = ofb(cipher_blocks, keys)

    counter = 0
    for input_bits, decoded_bits in zip(input_blocks, decoded_blocks):
        if input_bits == decoded_bits:
            counter +=1
    return counter == len(input_blocks)


# In[ ]:


def test_ctr(ctr):
    input_blocks = [BitArray('0b0111001011111100010100001111011010011001000010100110110000010100'),
    BitArray('0b0011000001011110010100001110110110110110101111010101011001010110'),
    BitArray('0b0110111011001111010010101100111111110010101110011110001011110000'),
    BitArray('0b0010000110001111100111001101001010011010101001111100010000000100'),
    BitArray('0b0110001111100011101011100011111000010011001100100001010110010011'),
    BitArray('0b0000000110111000111100000011001101000100010100001001111111001101'),
    BitArray('0b1010011001000111011100111000011101101011100000110011011001010010'),
    BitArray('0b0010100001111010101110001100010110110100101101000011000001100100'),
    BitArray('0b0110101100010001101100111000101011011101001111110101001110101101'),
    BitArray('0b1001101011110001100101001101011100111001101110011011001000100000')]

    K = BitArray('0b1111100001101110011110000010110110001110101001010110100110111011')

    cipher_blocks = ctr(input_blocks, K)
    decoded_blocks = ctr(cipher_blocks, K)

    counter = 0
    for input_bits, decoded_bits in zip(input_blocks, decoded_blocks):
        if input_bits == decoded_bits:
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
    print("Grade: {0:.2f}".format((exam_grade/(len(test_functions) * 10)) * 100))
    

