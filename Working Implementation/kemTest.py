import oqs
import timeit

algs = oqs.get_supported_KEM_mechanisms()
algLen = len(algs)

def test (algorithm):
    kem = oqs.KeyEncapsulation(algorithm)
    startKey = timeit.timeit()
    for i in range (100):
        public_key = kem.generate_keypair()
    endKey = timeit.timeit()

    startEncap = timeit.timeit()
    for x in range (100):
        ciphertext, shared_secret_server = kem.encap_secret(public_key)
    endEncap = timeit.timeit()

    startDecap = timeit.timeit()
    for j in range (100):
        shared_secret_client = kem.decap_secret(ciphertext)
    endDecap = timeit.timeit()


    print('Total time to genKey is ',(endKey-startKey), 'and time for 1 is ',((endKey-startKey)/100))
    print()
    print('Total time to encapsulate is ',(endEncap-startEncap), 'and time for 1 is ',((endEncap-startEncap)/100))
    print()
    print('Total time to decapsulate is ' ,(endDecap-startDecap), 'and time for 1 is ',((endDecap-startDecap)/100))
    print()



for i in range(1,algLen):
    print (algs[i])
    test(algs[i])