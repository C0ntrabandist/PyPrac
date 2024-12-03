import sys
import struct

b = sys.stdin.buffer.read()
len = len(b)

ch4na8 = struct.unpack("i", b[4:8])[0]
dva20na22 = struct.unpack("h", b[20:22])[0]
dva22na24 = struct.unpack("h", b[22:24])[0]
dva24na28 = struct.unpack("i", b[24:28])[0]
tri34na36 = struct.unpack("h", b[34:36])[0]
so40na44 = struct.unpack("i", b[40:44])[0]

a = [len < 44, 
     b[:4] != b"RIFF", ch4na8 != len - 8, 
     b[8:12] != b"WAVE",  
     b[12:16] != b"fmt "]

a += [struct.unpack("i", b[16:20])[0] != 16, 
      (dva24na28 != 44100 and dva24na28 != 48000), 
      struct.unpack("i", b[28:32])[0] != (dva24na28 * tri34na36 * dva22na24) / 8]

a += [struct.unpack("h", b[32:34])[0] != (tri34na36 * dva22na24) / 8, 
      struct.unpack("h", b[32:34])[0] not in {1, 2, 4}, 
      b[36:40] != b"data", so40na44 != ch4na8 - 36]

if any(a):
    print("NO")
else:
    print(f"Size={ch4na8}, Type={dva20na22}, Channels={dva22na24}, Rate={dva24na28}, Bits={tri34na36}, Data size={so40na44}")