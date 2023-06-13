from matrix import encrypt, decrypt, gen_key, generate_random_character

import matplotlib.pyplot as plt
import time

import ast
import base64

from collections import Counter

def find_most_common_int(nested_array):
    # Flatten the nested array
    flattened_array = [num for sublist in nested_array for num in sublist]
    
    # Count the occurrences of each integer
    count = Counter(flattened_array)
    
    # Find the most common integer and its count
    most_common = count.most_common()[:10]
    
    return most_common


test = {
    'sample_size': False,
    'key_similarity': False,
    'sandbox': True,
}

if __name__ == '__main__':
    if test['sample_size']:
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
    elif test['key_similarity']:
        CONTENT =  'Hello, World!'
        KEY = gen_key()

        ENCRYPTED = encrypt(KEY, CONTENT)
        DECRYPTED = decrypt(KEY, ENCRYPTED)

        KEY = ast.literal_eval(base64.b64decode(KEY).decode("utf-8"))

        print(find_most_common_int(KEY))
    elif test['sandbox']:
        CONTENT =  'Hello, World!'
        KEY = gen_key()

        ENCRYPTED = encrypt(KEY, CONTENT)
        DECRYPTED = decrypt(KEY, ENCRYPTED)

        KEY = ast.literal_eval(base64.b64decode(KEY).decode("utf-8"))

        NEW_KEY = []

        for idx, x in enumerate(KEY):
            for idy, y in enumerate(x):
                KEY[idx][idy] = str(y)
            NEW_KEY.append(':'.join(x))
        NEW_KEY = '/'.join(NEW_KEY)

        print(NEW_KEY)