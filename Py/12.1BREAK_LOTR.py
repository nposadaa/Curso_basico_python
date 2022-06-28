# Ciclo while with "where was gondor..."

def run():
    has_gondor_arrived = input('Has gondor arrived? (Yes or No):' )

    while has_gondor_arrived == 'No':
        print('Where was gondor when the west fold fell? Where wasssss... 😠' )
        has_gondor_arrived = input('Has gondor arrived? (Yes or No):' )
    print('Come one, this is not LOTR, Gondor never arrived! 😆')


if __name__ == '__main__':
    run()