import numpy as np
import ast
import base64

import matplotlib.pyplot as plt
import time
import secrets
import string

def get_index(c, i = False, o = 0):
    """
    :param c: the character to be indexed
    :param i: wether or not to be inverted
    :return: a index of the input
    """

    INDEX = {'A': 0,'B': 1,	'C': 2,	'D': 3,	'E': 4,	'F': 5,	'G': 6,	'H': 7,	'I': 8,	'J': 9,	'K': 10,'L': 11,'M': 12,'N': 13,'O': 14,'P': 15,'Q': 16,'R': 17,'S': 18,'T': 19,'U': 20,'V': 21,'W': 22,'X': 23,'Y': 24,'Z': 25,'a': 26,'b': 27,'c': 28,'d': 29,'e': 30,'f': 31,'g': 32,'h': 33,'i': 34,'j': 35,'k': 36,'l': 37,'m': 38,'n': 39,'o': 40,'p': 41,'q': 42,'r': 43,'s': 44,'t': 45,'u': 46,'v': 47,'w': 48,'x': 49,'y': 50,'z': 51,'0': 52,'1': 53,'2': 54,'3': 55,'4': 56,'5': 57,'6': 58,'7': 59,'8': 60,'9': 61,'+': 62,'/': 63,'=': 64}

    if i:
        v = {value + o: key for key, value in INDEX.items()}
        return v[c]
    else:
        return INDEX[c] + o

def generate_random_character(l):
    """
    :param l: the amount of random characters
    :return: a string of random characters
    """
    a = string.ascii_letters + string.digits + string.punctuation
    rl = ''
    
    for _ in range(l):
        rc = secrets.choice(a)
        rl += rc
    
    return rl

def gen_key(SIZE=97):
    """
    :return: a base64 string
    """
    m = []
    for _ in range(SIZE):
        r = []
        for _ in range(SIZE - len(r)):
            r += [secrets.randbelow((SIZE*SIZE) * 10)]

        m.append(r)

    return base64.b64encode(str(m).encode("utf-8")).decode("utf-8")

def encrypt(k, b, SIZE=97):
    """
    :param key: the generated key for kyber-lcb-9409
    :param body: the content to be encrypted
    :return: a nested array of numbers
    """
    k = ast.literal_eval(base64.b64decode(k).decode("utf-8"))
    es = base64.b64encode(b.encode("utf-8")).decode("utf-8")

    ea = [get_index(x) for x in es]
    ea = [get_index(x) for x in str(len(ea))] + [get_index('=')] + ea

    c = max(97, (len(ea) + SIZE - 1) // SIZE)  # Calculate the number of columns required
    
    m = []
    for i in range(SIZE):
        r = ea[(i * c):((i * c) + c)]
        for _ in range(c - len(r)):
            d = get_index(secrets.choice([c for c in base64.b64encode(generate_random_character(15).encode("utf-8")).decode("utf-8").replace('=', '')]))
            r += [d]

        m.append(r)

    # Multiply key and body
    k = np.array(k)
    m = np.array(m)

    m = np.dot(np.array(k), m).tolist()

    return base64.b64encode(str(m).encode("utf-8")).decode("utf-8")
    
def decrypt(k, arr, SIZE=97):
    """
    :param k: the generated key for kyber-lcb-9409
    :param array: an array of nested arrays provided from encrypt()
    :return: the decrypted content
    """
    arr = np.array(ast.literal_eval(base64.b64decode(arr).decode("utf-8")))
    k = np.array(ast.literal_eval(base64.b64decode(k).decode("utf-8")))

    d = np.dot(np.linalg.inv(k), arr).tolist()
    d = sum([[round(e) for e in r] for r in d], [])
    
    l = ''
    for idx, x in enumerate(d):
        if x == get_index('='):
            d = d[(idx+1):]
            break
        l += get_index(x, True)
    
    e = ''.join(get_index(x, True) for x in d[:int(l)])
    b = base64.b64decode(e).decode("utf-8")

    return b

if __name__ == '__main__':

    RAN = generate_random_character(10)
    CONTENT =  'Hello, World!'
    SAMPLE_SIZE = 20
    KEY = gen_key()


    print(f'This may take a while (sampling {SAMPLE_SIZE}, in intervals of {len(RAN)})...')

    for x in range(SAMPLE_SIZE):
        CONTENT += RAN
        KEY = gen_key()
        
        start = time.process_time()
        ENCRYPTED = encrypt(KEY, CONTENT)
        DECRYPTED = decrypt(KEY, ENCRYPTED)
        end = time.process_time()

        plt.scatter(len(CONTENT), (end - start), color = 'green' if CONTENT == DECRYPTED else 'red')

    print('Done! please inspect graph.')

    plt.title('Time compared to size')
    plt.xlabel(f'Content length (interval of {len(RAN)})')
    plt.ylabel('Time taken (ms)')
    plt.show()