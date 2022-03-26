import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik('menginstall Tukang Ngambek...')
mengetik('menginstall Tukang Mutung...')
mengetik('menginstall Tukang Colmek...')
mengetik('menginstall Bocah Sangean...')
mengetik('menginstall BocahNjeleih...')
mengetik('menginstall April Tai...')
mengetik('menginstall April Babi...')
mengetik('menginstall April Asu...')
mengetik('menginstall Kesayangane Inu...')
mengetik('TUNGGU YA ANJING')
