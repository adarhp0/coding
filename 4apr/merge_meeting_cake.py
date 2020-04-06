import unittest


def merge_ranges(meetings):

    # Merge meeting ranges
    n=len(meetings)
    me=[]
    meetings.sort()
    for i in range(50):
        me.append(0)
    res=[]
    max_end=0
    ch=1
    for i in range(n-1):
        st_cr=meetings[i][0]
        ent_cr=meetings[i][1]
        st_nx=meetings[i+1][0]
        ent_nx=meetings[i+1][1]
        if max_end<ent_cr:
            max_end=ent_cr
        if ent_cr<st_nx:
            ch=ch+1
        if i!=0:
            if st_cr>meetings[i-1][1]:
                ch=ch+1
        for j in range(st_cr,ent_cr+1):
            if me[j]!=0:
                ch=me[j]
            me[j]=ch
    st_cr=meetings[-1][0]
    ent_cr=meetings[-1][1]
    st_pr=meetings[n-2][0]
    ent_pr=meetings[n-2][1]
    if max_end<ent_cr:
        max_end=ent_cr
    if st_cr>ent_pr:
        ch=ch+1
    for j in range(st_cr,ent_cr+1):
            me[j]=ch
    re=[]
    op=0
    va=-1
    
    for i in range(max_end+1):
        if me[i]!=0 and op==0:
            a1=i
            op=1
            va=me[i]
        elif me[i]==va and op==1 and i==max_end:
            b=0
            a2=i
            re.append((a1,a2))
        elif me[i]!=va and me[i]!=0 and op==1:
            a2=i-1
            va=me[i]
            re.append((a1,a2))
            a1=i
        elif me[i]==0 and op==1:
            a2=i-1
            re.append((a1,a2))
            op=0
    #print(re)
    return re
"""
best solution follows greedy"""

def merge_ranges(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings















# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)