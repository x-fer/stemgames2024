import mido


l = []

mid = mido.MidiFile('../upload/audio.mid')
for msg in mid:
    if msg.type == 'note_on':
        print(msg.note)
        if msg.note == 60:
            l.append(0)
        elif msg.note == 72:
            l.append(1)


# 8 by 8
l = [l[i:i+8] for i in range(0, len(l), 8)]

# bin to char
l = [chr(int("".join(map(str, x)), 2)) for x in l]

print("".join(l))
