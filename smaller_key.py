import base64
import secrets
import string
import binascii

from collections import Counter

def find_most_common_combination(string, combination_length):
    combinations = [string[i:i+combination_length] for i in range(len(string)-combination_length+1) if ':' not in string[i:i+combination_length] and '|' not in string[i:i+combination_length]]
    combination_counts = Counter(combinations)
    most_common = combination_counts.most_common(10)
    return most_common if most_common else None

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

def compress(m):

    for idx, x in enumerate(m):
        m[idx] = ':'.join(x)

    m = '|'.join(m)

    m = m.replace('39','a').replace('28','b').replace('35','c').replace('37','d').replace('11','e').replace('24','f').replace('27','g').replace('20','h').replace('30','i').replace('26','j').replace('34','k').replace('36','l').replace('38','m').replace('29','n').replace('25','o').replace('10','p').replace('18','q').replace('15','r').replace('17','s').replace('19','t').replace('16','u').replace('14','v').replace('40','w').replace('80','x').replace('77','y').replace('66','z')
    m = m.replace('55','A').replace('89','B').replace('49','C').replace('60','D').replace('50','E').replace('79','F').replace('70','G').replace('69','H').replace('59','I').replace('88','J').replace('44','K').replace('78','L').replace('54','M').replace('64','N').replace('74','O').replace('68','P').replace('58','Q').replace('65','R').replace('90','S').replace('33','T').replace('22','U').replace('67','V').replace('75','W').replace('48','X').replace('32','Y').replace('12','Z')
    m = m.replace('13','~').replace('85','`').replace('57','!').replace('84','@').replace('76','#').replace('23','$').replace('56','%').replace('45','^').replace('47','&').replace('87','*').replace('46','(').replace('86',')').replace('31','-').replace('21','_').replace('99','+').replace('00','=').replace('62','{').replace('72','}').replace('63','[').replace('52','[').replace('73','\\').replace('53','/').replace('42',';').replace('83','"').replace('82','\'').replace('43','<')
    m = m.replace('61','>').replace('93',',').replace('71','.').replace('92','?')

    return m

def compress2(m):

    for idx, x in enumerate(m):
        m[idx] = ':'.join(x)

    m = '|'.join(m)

    m = m.replace('764','a').replace('841','b').replace('860','c').replace('452','d').replace('295','e').replace('198','f').replace('470','g').replace('213','h').replace('377','i').replace('210','j').replace('170','k').replace('385','l').replace('366','m').replace('611','n').replace('265','o').replace('636','p').replace('975','q').replace('669','r').replace('559','s').replace('570','t').replace('299','u').replace('450','v').replace('940','w').replace('220','x').replace('867','y').replace('194','z')
    m = m.replace('334','A').replace('999','B').replace('267','C').replace('830','D').replace('280','E').replace('380','F').replace('218','G').replace('880','H').replace('823','I').replace('240','J').replace('760','K').replace('910','L').replace('234','M').replace('320','N').replace('150','O').replace('270','P').replace('627','Q').replace('260','R').replace('196','S').replace('350','T').replace('870','U').replace('840','V').replace('630','W').replace('790','X').replace('310','Y').replace('330','Z')
    m = m.replace('289','~').replace('395','`').replace('190','!').replace('740','@').replace('167','#').replace('890','$').replace('390','%').replace('285','^').replace('225','&').replace('250','*').replace('820','(').replace('290',')').replace('244','-').replace('810','_').replace('375','+').replace('120','=').replace('430','{').replace('480','}').replace('140','[').replace('370','[').replace('970','\\').replace('730','/').replace('264',';').replace('249','"').replace('930','\'').replace('160','<')
    #m = m.replace('','>').replace('',',').replace('','.').replace('','?')

    return m

def decompress(m):

    m = m.replace('a','39').replace('b','28').replace('c','35').replace('d','37').replace('e','11').replace('f','24').replace('g','27').replace('h','20').replace('i','30').replace('j','26').replace('k','34').replace('l','36').replace('m','38').replace('n','29').replace('o','25').replace('p','10').replace('q','18').replace('r','15').replace('s','17').replace('t','19').replace('u','16').replace('v','14').replace('w','40').replace('x','80').replace('y','77').replace('z','66')
    m = m.replace('A','55').replace('B','89').replace('C','49').replace('D','60').replace('E','50').replace('F','79').replace('G','70').replace('H','69').replace('I','59').replace('J','88').replace('K','44').replace('L','78').replace('M','54').replace('N','64').replace('O','74').replace('P','68').replace('Q','58').replace('R','65').replace('S','90').replace('T','33').replace('U','22').replace('V','67').replace('W','75').replace('X','48').replace('Y','32').replace('Z','12')
    m = m.replace('~','13').replace('`','85').replace('!','57').replace('@','84').replace('#','76').replace('$','23').replace('%','56').replace('^','45').replace('&','47').replace('*','87').replace('(','46').replace(')','86').replace('-','31').replace('_','21').replace('+','99').replace('=','00').replace('{','62').replace('}','72').replace('[','63').replace(']','52').replace('\\','73').replace('/','53').replace(';','42').replace('"','83').replace('\'','82').replace('<','43')
    m = m.replace('>','61').replace(',','93').replace('.','71').replace('?','92')
    
    m = m.split('|')

    for idx, x in enumerate(m):
        m[idx] = x.split(':')

    return m


def new_gen_key(comp2, SIZE=97):
    """
    :return: a base64 string
    """
    m = []
    for _ in range(SIZE):
        r = []
        for _ in range(SIZE - len(r)):
            r += [str(secrets.randbelow(1000000000))]

        m.append(r)

    if comp2:
        return compress2(m)
    else:
        return compress(m)


def original_gen_key(SIZE=97):
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

if __name__ == '__main__':
    O_KEY = original_gen_key()
    N1_KEY = new_gen_key(False)
    N2_KEY = new_gen_key(True)

    large_key = ''
    for x in range(100):
        print(f'{x+1}/100')
        large_key += new_gen_key(True)
    
    print(find_most_common_combination(large_key, 3))

    print('\nOriginal\t :', len(O_KEY))
    print('Compression 1\t :', len(N1_KEY), f'o/c1({(len(O_KEY) - len(N1_KEY)) * -1})')
    print('Compression 2\t :', len(N2_KEY), f'o/c2({(len(O_KEY) - len(N2_KEY)) * -1}), c1/c2({(len(N1_KEY) - len(N2_KEY)) * -1})')
