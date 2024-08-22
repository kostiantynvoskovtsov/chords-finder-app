# Major chords marked with capital letters
notes = ['C', 'd', 'e', 'F', 'G', 'a', 'b']
chord_name = str(input('Please enter chord name and find out whether it is Major or minor! '))

# Normalize input to handle non-capitalized major chords
normalized_chord = chord_name.upper()

# Check for major chords or diminished chord
if normalized_chord == 'C':
    print('Your chord is C major 7')
elif normalized_chord == 'F':
    print('Your chord is F major 7')
elif normalized_chord == 'G':
    print('Your chord is G major 7')
elif chord_name == 'b':
    print('Your chord is b diminished 7')
else:
    print(f'Your chord is {chord_name} minor 7')

# Guitar chord positions based on bass string
bass_string = int(input('Please choose bass string for the chord (5 or 6): '))

# Finger positions for bass string 5
if bass_string == 5:
    if normalized_chord == 'C':
        print('3rd fret on 1st string\n5th fret on 2nd string\n4th fret on 3rd string\n5th fret on 4th string\n3rd fret on 5th string')
    elif normalized_chord == 'F':
        print('8th fret on 1st string\n10th fret on 2nd string\n9th fret on 3rd string\n10th fret on 4th string\n8th fret on 5th string')
    elif normalized_chord == 'G':
        print('10th fret on 1st string\n12th fret on 2nd string\n11th fret on 3rd string\n12th fret on 4th string\n10th fret on 5th string')
    elif chord_name == 'd':
        print('5th fret on 1st string\n6th fret on 2nd string\n5th fret on 3rd string\n7th fret on 4th string\n5th fret on 5th string')
    elif chord_name == 'e':
        print('7th fret on 1st string\n8th fret on 2nd string\n7th fret on 3rd string\n9th fret on 4th string\n7th fret on 5th string')
    elif chord_name == 'a':
        print('12th fret on 1st string\n13th fret on 2nd string\n12th fret on 3rd string\n14th fret on 4th string\n12th fret on 5th string')
    elif chord_name == 'b':
        print('14th fret on 1st string\n15th fret on 2nd string\n14th fret on 3rd string\n15th fret on 4th string\n14th fret on 5th string')

# Finger positions for bass string 6
if bass_string == 6:
    if normalized_chord == 'C':
        print('8th fret on 1st string\n8th fret on 2nd string\n9th fret on 3rd string\n9th fret on 4th string\n10th fret on 5th string\n8th fret on 6th string')
    elif normalized_chord == 'F':
        print('1st fret on 1st string\n1st fret on 2nd string\n2nd fret on 3rd string\n2nd fret on 4th string\n3rd fret on 5th string\n1st fret on 6th string')
    elif normalized_chord == 'G':
        print('3rd fret on 1st string\n3rd fret on 2nd string\n4th fret on 3rd string\n4th fret on 4th string\n5th fret on 5th string\n3rd fret on 6th string')
    elif chord_name == 'd':
        print('10th fret on 1st string\n10th fret on 2nd string\n10th fret on 3rd string\n10th fret on 4th string\n12th fret on 5th string\n10th fret on 6th string')
    elif chord_name == 'e':
        print('12th fret on 1st string\n12th fret on 2nd string\n12th fret on 3rd string\n12th fret on 4th string\n14th fret on 5th string\n12th fret on 6th string')
    elif chord_name == 'a':
        print('5th fret on 1st string\n5th fret on 2nd string\n5th fregit init')