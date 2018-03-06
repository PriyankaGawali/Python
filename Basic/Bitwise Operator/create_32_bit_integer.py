#WAP to accept following values from user. CRC, length, data and flag where
#CRC is 5 bits,     (e.g. 7 i.e. 00111)
#length is 8 bits   (e.g.12 i.e. 00001100)
#data is 18 bits and  (e.g. 145 i.e. 000000000010010001)
#flag is 1 bit.  (e.g. 0 i.e. 0)
#Then packet is 00111000011000000000000100100010
# (Total 32 bits)
#packet value = 945815842


def de_packet(packet):
    # remove flag  bit
    flag_value = packet & ((1 << 1) - 1)

    # delete flag bit from packet
    packet = packet >> 1

    # remove data bit
    data_value = packet & ((1 << 18) - 1)

    # delete data bit from packet
    packet = packet >> 18

    # remove length bit
    length_value = packet & (( 1 << 8) - 1)

    # delete length bit from paket
    packet = packet >> 8

    #remove crc bit
    crc_value = packet & ((1 << 5) - 1)

    return crc_value, length_value, data_value, flag_value


def create_packet(crc_value, len_value, data_value, flag_value):
    # first assign crc_value to packet
    packet = crc_value

    # create 8 space for length_value
    packet = packet << 8

    # add length_value to packet
    packet = packet | len_value & ((1 << 8) - 1)

    # create space for 18 bits
    packet = packet << 18

    # add data_value to packet
    packet = packet | data_value & ((1 << 18) - 1)

    # create space for 1 bit
    packet = packet << 1


    # add flag_value to packet
    packet = packet | flag_value & ((1 << 1) - 1)

    return packet


def main():
    crc = int(input("Enter crc : "))
    length = int(input("Enter length : "))
    data = int(input("Enter data : "))
    flag = int(input("Enter flag : "))
    packet_value = create_packet(crc, length, data, flag)
    print("Packet value : ", create_packet(crc, length, data, flag))
    print("After De- packetizing ", de_packet(packet_value))


if __name__ == '__main__':
    main()
